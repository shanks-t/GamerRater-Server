# Generated by Django 3.2.9 on 2021-11-12 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamer_rater_api', '0004_alter_gameimage_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='categories',
            field=models.ManyToManyField(to='gamer_rater_api.Category'),
        ),
    ]