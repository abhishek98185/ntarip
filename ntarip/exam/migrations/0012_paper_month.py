# Generated by Django 5.2 on 2025-05-27 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0011_rename_number_paper_shift'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='month',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
