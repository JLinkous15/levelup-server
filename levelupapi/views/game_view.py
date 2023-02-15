"""View module for handling requests about games"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game

class GameView(ViewSet):
    
    def list(self, request):
        """Handles GET all requests from the Game table
        Returns an instance from the Response class with an array of objects and a status code of 200"""
        games = Game.objects.all()
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        """Handles GET requests from the Game table based on the primary key.
        Returns an instance from the Response class with an object and a status code of 200"""
        game = Game.objects.get(pk=pk)
        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_200_OK)

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id','name','description','game_type','creator', 'number_of_players','skill_level')