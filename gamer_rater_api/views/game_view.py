from typing import Reversible
from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from gamer_rater_api.models import Game, Category, GameCategory, Review, GameRating


class GameView(ViewSet):

    def list(self, request):
        games = Game.objects.all()

        serializer = GameSerializer(
            games, many=True, context={'request': request})
        return Response(serializer.data)


    def retrieve(self, request, pk=None):
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        # category_id = GameCategory.objects.get(pk=request.data['categoryId'])
        category = Category.objects.get(pk=request.data['categoryId'])
        
        try:
            game = Game.objects.create(
                title=request.data['title'],
                designer=request.data['designer'],
                year_released=request.data['yearReleased'],
                age_recommendation=request.data['ageRecommendation'],
                play_time =request.data['playTime']
            )
            # game.categories.set(request.data['category_ids'])
            game.categories.add(category)
            serializer = GameSerializer(game, context={'request': request})
            return Response(serializer.data)
        
        except ValidationError as ex:
            return Response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)

    @property
    def average_rating(self):
        """Average rating calculated attribute for each game"""
        ratings = GameRating.objects.filter(game=self)

        # Sum all of the ratings for the game
        total_rating = 0
        count = 0
        for rating in ratings:
            total_rating += rating.rating
            count += 1

        average = total_rating/count
        return self.average_rating.add(average)
        

        # Calculate the averge and return it.
        # If you don't know how to calculate averge, Google it.

class RatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameRating
        fields = ('id', 'rating')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'label')

class ReviewSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Review
        fields = ('id', 'title', 'game_review', 'game_id', 'player_id')

class GameSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    reviews = ReviewSerializer(many=True)
    ratings = RatingsSerializer(many=True)
    class Meta:
        model = Game
        fields = ('id', 'title', 'designer', 'year_released', 'play_time', 'age_recommendation', 'categories', 'reviews', 'ratings')