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

    @property
    def average_rating(self):
        """Average rating calculated attribute for each game"""
        ratings = GameRating.objects.filter(game_id=self.id)
        # Sum all of the ratings for the game
        total_rating = 0
        if ratings:
            for rating in ratings:
                total_rating += rating.rating
            average = total_rating / len(ratings)
        else:
            average = 0
            

        return average

        # Calculate the averge and return it.
        # If you don't know how to calculate averge, Google it.
