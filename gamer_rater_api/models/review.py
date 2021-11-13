from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=55)
    game_review = models.TextField()
    game_rating = models.IntegerField(default=0)
    player_id = models.ForeignKey("Player", on_delete=models.CASCADE)
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE, related_name='reviews')

def __str__(self):
    return self.title 