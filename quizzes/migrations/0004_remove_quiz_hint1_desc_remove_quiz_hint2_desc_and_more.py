# Generated by Django 5.0.4 on 2024-05-03 08:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0003_quiz_hint1_desc_quiz_hint2_desc_quiz_hint3_desc'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='hint1_desc',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='hint2_desc',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='hint3_desc',
        ),
    ]
