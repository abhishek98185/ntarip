# Generated by Django 5.2 on 2025-05-26 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_paper_dummy_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paper',
            name='dummy_field',
        ),
        migrations.AddField(
            model_name='paper',
            name='paper_number',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='paper',
            name='paper_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
