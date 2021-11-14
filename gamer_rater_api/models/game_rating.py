from django.db import models

class GameRating(models.Model):
    rating = models.IntegerField()
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)
    player_id = models.ForeignKey("Player", on_delete=models.CASCADE)


