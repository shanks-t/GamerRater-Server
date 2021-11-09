from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=55)
    designer = models.CharField(max_length=55)
    year_released = models.IntegerField()
    play_time = models.IntegerField()
    age_recomendation = models.IntegerField()
