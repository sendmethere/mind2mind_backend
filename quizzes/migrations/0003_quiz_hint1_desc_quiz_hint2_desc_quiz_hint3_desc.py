# Generated by Django 5.0.4 on 2024-05-03 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_alter_quiz_fail_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='hint1_desc',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='hint2_desc',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='hint3_desc',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]