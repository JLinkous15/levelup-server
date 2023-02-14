from django.db import models


class Event(models.Model):

    host = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name="host")
    game = models.ManyToManyField("Game", related_name = "event_games")
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
