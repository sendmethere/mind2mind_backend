from rest_framework import serializers
from .models import Player
from quizzes.models import Quiz

class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['id', 'access_code', 'author']

class PlayerSerializer(serializers.ModelSerializer):
    
    created_quizzes = QuizSerializer(many=True, read_only=True)
    success_quizzes = QuizSerializer(many=True, read_only=True)
    
    class Meta:
        model = Player
        fields = '__all__'