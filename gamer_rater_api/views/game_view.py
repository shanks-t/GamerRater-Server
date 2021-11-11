from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from gamer_rater_api.models import Game, Category


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
        category = Category.objects.get(pk=request.data['categoryId'])


        try:
            game = Game.objects.create(
                title=request.data['title'],
                designer=request.data['designer'],
                year_released=request.data['yearReleased'],
                age_recommendation=request.data['ageRecommendation'],
                category=category
            )
            serializer = GameSerializer(game, context={'request': request})
            return Response(serializer.data)
        
        except ValidationError as ex:
            return Response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)




class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'title', 'designer', 'year_released', 'play_time', 'age_recommendation')