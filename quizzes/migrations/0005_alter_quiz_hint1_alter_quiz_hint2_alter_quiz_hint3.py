# Generated by Django 5.0.4 on 2024-05-03 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0004_remove_quiz_hint1_desc_remove_quiz_hint2_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='hint1',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='hint2',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='hint3',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
