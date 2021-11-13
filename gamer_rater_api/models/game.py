from django.db import models
from gamer_rater_api.models.category import Category
from gamer_rater_api.models.game_rating import GameRating

class Game(models.Model):
    title = models.CharField(max_length=55)
    designer = models.CharField(max_length=55)
    year_released = models.IntegerField()
    play_time = models.DecimalField(max_digits=5, decimal_places=2)
    age_recommendation = models.IntegerField()
    categories = models.ManyToManyField(Category)
    average_rating = models.IntegerField(default=0)

    def __str__(self):
        return self.title 