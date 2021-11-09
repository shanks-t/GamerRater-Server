from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=55)
    game_review = models.TextField()
    game_rating = models.IntegerField()
    player_id = models.ForeignKey("Player", on_delete=models.CASCADE)
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)

