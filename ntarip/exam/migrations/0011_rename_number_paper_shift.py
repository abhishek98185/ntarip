# Generated by Django 5.2 on 2025-05-27 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0010_remove_questionandoptions_paper_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paper',
            old_name='number',
            new_name='shift',
        ),
    ]
