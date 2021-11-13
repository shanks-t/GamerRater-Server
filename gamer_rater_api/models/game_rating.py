from django.db import models

class GameRating(models.Model):
    rating = models.IntegerField()
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='ratings')
    player_id = models.ForeignKey("Player", on_delete=models.CASCADE)
