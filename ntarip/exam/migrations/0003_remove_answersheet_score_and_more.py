# Generated by Django 5.2 on 2025-05-26 07:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0002_remove_useranswer_user_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answersheet',
            name='score',
        ),
        migrations.RemoveField(
            model_name='answersheet',
            name='total_questions',
        ),
        migrations.AlterField(
            model_name='answersheet',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exam.paper'),
        ),
        migrations.AlterField(
            model_name='questionandoptions',
            name='answer',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='answer',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='useranswer',
            name='answersheet',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exam.answersheet'),
        ),
    ]
