"""View module for handling requests about events"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event, Game, Gamer


class EventView(ViewSet):
    
    def list(self, request):
        """Handles GET requests for a single event based on the primary key
        Returns a Response instance containing the Event and a status code of 200"""
        
        events = Event.objects.all()
        for event in events:
            event.is_host = False
            if event.host.user == request.auth.user:
                event.is_host = True
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
    
    def create(self, request):
        """Handles POST requests to events
        Returns the posted object, including pk"""
        host = Gamer.objects.get(user = request.auth.user)
        game = Game.objects.get(pk = request.data['game'])
        new_event = Event.objects.create(
            host = host,
            game = game,
            date = request.data['date'],
            location = request.data['location']
        )
        serializer = EventSerializer(new_event)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """Handles PUT requests to /events/pk"""
        event = Event.objects.get(pk=pk)
        game = Game.objects.get(pk = request.data['game'])
        event.game=game
        event.date = request.data['date']
        event.location = request.data['location']
        event.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)

    def destroy(self, request, pk):
        event = Event.objects.get(pk=pk)
        event.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

        
class EventGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id','name','description','game_type','creator', 'number_of_players','skill_level')

class EventGamerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gamer
        fields = ('id','full_name','bio')

class EventSerializer(serializers.ModelSerializer):
    host = EventGamerSerializer(many=False)
    game = EventGameSerializer(many=False)
    attendance = EventGamerSerializer(many=True)
    class Meta:
        model = Event
        fields = ('id','host','game','attendance','date','location', 'is_host')