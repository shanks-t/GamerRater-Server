from django.contrib import admin
from gamer_rater_api.models import GameImage, Category, Player, Review, Game

# Register your models here.
admin.site.register(GameImage)
admin.site.register(Game)
admin.site.register(Player)
admin.site.register(Review)
admin.site.register(Category)