# Generated by Django 3.2.9 on 2021-11-13 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gamer_rater_api', '0012_alter_game_average_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='average_rating',
        ),
    ]