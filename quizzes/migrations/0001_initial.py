# Generated by Django 5.0.4 on 2024-04-26 06:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(choices=[('3emoji', '3 Emoji'), ('4+emoji', '4 or more Emoji'), ('3hint', '3 Hint')], max_length=10)),
                ('access_code', models.CharField(max_length=7, unique=True)),
                ('hint_text', models.CharField(blank=True, max_length=30, null=True)),
                ('hint1', models.CharField(blank=True, max_length=30, null=True)),
                ('hint2', models.CharField(blank=True, max_length=30, null=True)),
                ('hint3', models.CharField(blank=True, max_length=30, null=True)),
                ('answer', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ManyToManyField(related_name='quizzes', to='players.player')),
                ('fail_user', models.ManyToManyField(related_name='fail_quizzes', to='players.player')),
            ],
        ),
        migrations.CreateModel(
            name='SuccessRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='players.player')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizzes.quiz')),
            ],
        ),
        migrations.AddField(
            model_name='quiz',
            name='success_user',
            field=models.ManyToManyField(related_name='success_quizzes', through='quizzes.SuccessRecord', to='players.player'),
        ),
    ]