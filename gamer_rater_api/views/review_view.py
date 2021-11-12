from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from gamer_rater_api.models import Review, Player, Game
class ReviewView(ViewSet):

    def create(self, request):
        # category_id = GameCategory.objects.get(pk=request.data['categoryId'])
        player = Player.objects.get(pk=request.data['playerId'])
        game = Game.objects.get(pk=request.data['gameId'])

        try:
            review = Review.objects.create(
                title=request.data['title'],
                game_review=request.data['gameReview'],
                game_rating=request.data['gameRating'],
                player_id=player,
                game_id=game
            )
            serializer = ReviewSerializer(review, context={'request': request})
            return Response(serializer.data)
        
        except ValidationError as ex:
            return Response({'reason': ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        reviews = Review.objects.all()

        serializer = ReviewSerializer(
            reviews, many=True, context={'request': request})
        return Response(serializer.data)

class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id', 'title', 'game_review', 'game_rating', 'game_id', 'player_id']