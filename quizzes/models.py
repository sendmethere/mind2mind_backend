from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from players.models import Player
import random
from django.db.models import JSONField


class Quiz(models.Model):
    TYPE_CHOICES = [
        ('3emoji', '3 Emoji'),
        ('4+emoji', '4 or more Emoji'),
        ('3hint', '3 Hint')
    ]

    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    access_code = models.CharField(max_length=7, unique=True)
    hint_text = models.CharField(max_length=30, null=True, blank=True)
    hint1 = JSONField(null=True, blank=True)
    hint2 = JSONField(null=True, blank=True)
    hint3 = JSONField(null=True, blank=True)
    author = models.ManyToManyField(Player, related_name='quizzes')
    answer = models.CharField(max_length=30)
    success_user = models.ManyToManyField(Player, through='SuccessRecord', related_name='success_quizzes')
    fail_user = models.ManyToManyField(Player, related_name='fail_quizzes', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.access_code}] {self.type} Quiz by {', '.join([author.nickname for author in self.author.all()])}"

    def save(self, *args, **kwargs):
        if not self.access_code:
            self.access_code = self.generate_access_code()
        
        if 'author_nickname' in kwargs:
            author_nickname = kwargs.pop('author_nickname')
            author, created = Player.objects.get_or_create(nickname=author_nickname)
            super().save(*args, **kwargs)
            self.author.add(author)
        else:
            super().save(*args, **kwargs)

    def generate_access_code(self):
        code = ''.join([str(random.randint(0, 9)) for _ in range(7)])
        while Quiz.objects.filter(access_code=code).exists():
            code = ''.join([str(random.randint(0, 9)) for _ in range(7)])
        return code

class SuccessRecord(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
