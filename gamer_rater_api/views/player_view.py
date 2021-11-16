from django.core.exceptions import ValidationError
from rest_framework import status
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from gamer_rater_api.models import Review, Player, Game


class PlayerView(ViewSet):

 def retrieve(self, request, pk=None):
        player = Player.objects.get(pk=pk)
        serializer = PlayerSerializer(player, context={'request': request})
        return Response(serializer.data)


class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player
        fields = ('id', 'name')