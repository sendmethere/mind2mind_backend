from rest_framework import serializers
from .models import Quiz, SuccessRecord
from players.serializers import PlayerSerializer

class QuizSerializer(serializers.ModelSerializer):
    author = PlayerSerializer(many=True, read_only=True)
    success_user = PlayerSerializer(many=True, read_only=True)
    fail_user = PlayerSerializer(many=True, read_only=True)

    class Meta:
        model = Quiz
        fields = '__all__'
        read_only_fields = ('access_code',)

class SuccessRecordSerializer(serializers.ModelSerializer):
    player = PlayerSerializer(read_only=True)
    quiz = QuizSerializer(read_only=True)

    class Meta:
        model = SuccessRecord
        fields = '__all__'
