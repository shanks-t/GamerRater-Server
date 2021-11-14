from typing import Reversible
from django.core.exceptions import ValidationError
from django.db.models.fields import IntegerField
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from gamer_rater_api.models import Game, Category, GameCategory, Review, GameRating


class GameView(ViewSet):

    def create(self, request):
            # category_id = GameCategory.objects.get(pk=request.data['categoryId'])
        game = Game.objects.get(pk=pk)
        game_rating = GameRating.objects.create(
            rating=request.data['rating'],
            game_id = game.id
        )
        serializer = RatingsSerializer(game_rating, context={'request': request})
        return Response(serializer.data)

class RatingsSerializer(serializers.ModelSerializer):

    class Meta:
        model = GameRating
        fields = ('id', 'rating', 'game_id', 'player_id')