from django.shortcuts import render
from django.http import JsonResponse
import json

from rest_framework import viewsets, status
from rest_framework import generics

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Quiz, SuccessRecord, Player
from .serializers import QuizSerializer, SuccessRecordSerializer
from players.serializers import PlayerSerializer

import random

class QuizViewSet(viewsets.ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    @action(detail=True, methods=['post'])
    def success(self, request, pk=None):
        quiz = self.get_object()
        player_id = request.data.get('player_id')
        player = Player.objects.get(id=player_id)

        # 성공 기록 중복 확인
        if quiz.success_user.filter(id=player.id).exists() or quiz.fail_user.filter(id=player.id).exists():
            return Response({'message': 'Player already recorded or has failed this quiz.'}, status=status.HTTP_409_CONFLICT)
        
        # 성공 기록 추가
        SuccessRecord.objects.create(player=player, quiz=quiz)
        quiz.success_user.add(player)
        return Response({'message': 'Success recorded'}, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'], url_path='by-access-code/(?P<access_code>[^/.]+)')
    def get_by_access_code(self, request, access_code=None):
        quiz = Quiz.objects.filter(access_code=access_code).first()
        if quiz is not None:
            serializer = self.get_serializer(quiz)
            return Response(serializer.data)
        else:
            return Response({"message": "Quiz not found with the provided access code"}, status=status.HTTP_404_NOT_FOUND)

    @action(detail=True, methods=['post'])
    def fail(self, request, pk=None):
        quiz = self.get_object()
        player_id = request.data.get('player_id')
        player = Player.objects.get(id=player_id)

        # 실패 기록 중복 확인
        if quiz.fail_user.filter(id=player.id).exists():
            return Response({'message': 'Player already failed this quiz.'}, status=status.HTTP_409_CONFLICT)
        
        # 실패 기록 추가
        quiz.fail_user.add(player)
        return Response({'message': 'Failure recorded'}, status=status.HTTP_201_CREATED)
    
    def perform_create(self, serializer):
        author_nickname = self.request.data.get('author_nickname')
        if not author_nickname:
            return Response({'error': 'Nickname is required'}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()  # 일단 퀴즈 저장

        author, created = Player.objects.get_or_create(nickname=author_nickname)
        quiz = serializer.instance
        quiz.author.add(author)  # author 추가
        quiz.save()

class PlayerSuccessRecordsView(generics.ListAPIView):
    serializer_class = SuccessRecordSerializer
    queryset = SuccessRecord.objects.all()

    def get_queryset(self):
        nickname = self.kwargs['nickname']
        return self.queryset.filter(player__nickname=nickname).order_by('-timestamp')[:10]
    
    from django.http import JsonResponse
from .models import Player, Quiz, SuccessRecord

@api_view(['POST'])
def add_success_user(request):
    try:
        data = json.loads(request.body)
        nickname = data.get('nickname').strip('"')
        quiz_id = data.get('quizId')
        quiz = Quiz.objects.get(id=quiz_id)
        player, created = Player.objects.get_or_create(nickname=nickname)
        
        print("Received nickname:", nickname)
        quiz.success_user.add(player)
        return Response({'message': 'Player added to success list.'}, status=status.HTTP_200_OK)
    except Quiz.DoesNotExist:
        return Response({'error': 'Quiz not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def get_random_quizzes(request):
    latest_quizzes = Quiz.objects.all().order_by('-created_at')[:50]
    random_quizzes = random.sample(list(latest_quizzes), 4)
    serializer = QuizSerializer(random_quizzes, many=True)
    return Response(serializer.data)

## 통계 가져오기 ##

@api_view(['GET'])
def get_player_statistics(request, nickname):
    try:
        nickname = nickname.strip('"')
        player = Player.objects.get(nickname=nickname)
        serializer = PlayerSerializer(player)
        return Response(serializer.data)
    except Player.DoesNotExist:
        return Response({'error': 'Player not found'}, status=status.HTTP_404_NOT_FOUND)