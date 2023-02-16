from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Gamer

class GamerView(ViewSet):
    """Handles HTTP requests to /gamers"""
    def list(self, request):
        gamers = Gamer.objects.all()
        serialized = GamerSerializer(gamers, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        gamer = Gamer.objects.get(pk=pk)
        serialized = GamerSerializer(gamer)
        return Response(serialized.data, status=status.HTTP_200_OK)
    
class GamerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Gamer
        fields=('full_name', 'bio')