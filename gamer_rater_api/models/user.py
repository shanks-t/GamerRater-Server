from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=55)
    password = models.CharField(max_length=55)
    email = models.EmailField
    player_id = models.ForeignKey("Player", on_delete=models.CASCADE)
