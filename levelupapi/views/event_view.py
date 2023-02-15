"""View module for handling requests about events"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, Game

class EventView(ViewSet):
    
    def list(self, request):
        """Handles GET requests for a single event based on the primary key
        Returns a Response instance containing the Event and a status code of 200"""
        
        events = Event.objects.all()

        if "game" in request.query_params:
            game_obj = Game.objects.get(pk=request.query_params['game'])
            events = events.filter(game = game_obj)
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        

    def retrieve(self, request, pk):
        """Handles GET requests for a list of event objects based on the primary key
        Returns a Response instance containing the Event array and a status code of 200"""
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EventSerializer(serializers.ModelSerializer):

    class Meta():
        model = Event
        fields = ('id','host','game','attendance','date','location')