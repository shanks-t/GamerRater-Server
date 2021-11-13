# Generated by Django 3.2.9 on 2021-11-13 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamer_rater_api', '0010_game_average_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gamerating',
            name='game_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='gamer_rater_api.game'),
        ),
    ]
