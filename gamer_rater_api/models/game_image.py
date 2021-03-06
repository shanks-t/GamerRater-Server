from django.db import models

class GameImage(models.Model):
    image = models.ImageField(blank=True, null=True)
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)
    player_id = models.ForeignKey("Player", on_delete=models.CASCADE)
