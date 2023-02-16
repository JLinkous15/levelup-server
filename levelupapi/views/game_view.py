"""View module for handling requests about games"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Game, Gamer, GameType

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

    def create(self, request):
        game_type = GameType.objects.get(pk=request.data["game_type"])

        game = Game.objects.create(
            name = request.data['name'],
            description = request.data['description'],
            game_type = game_type,
            creator = request.data['creator'],
            number_of_players = request.data['number_of_players'],
            skill_level = request.data['skill_level']
        )
        serializer = GameSerializer(game)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handles PUT requests to games"""
        game = Game.objects.get(pk=pk)
        game.description=request.data["description"]
        game.creator=request.data["creator"]
        game.number_of_players=request.data["number_of_players"]
        game.skill_level=request.data["skill_level"]
        game.name=request.data["name"]
        
        game_type=GameType.objects.get(pk=request.data['game_type'])
        game.game_type = game_type

        game.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id','name','description','game_type','creator', 'number_of_players','skill_level')