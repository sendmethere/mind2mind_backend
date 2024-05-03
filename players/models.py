from django.db import models

class Player(models.Model):
    nickname = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.nickname