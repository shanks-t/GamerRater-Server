from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=55)
    designer = models.CharField(max_length=55)
    year_released = models.IntegerField()
    play_time = models.DecimalField(max_digits=5, decimal_places=2)
    age_recommendation = models.IntegerField()

    def __str__(self):
        return self.title 