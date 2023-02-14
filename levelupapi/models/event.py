from django.db import models


class Event(models.Model):

    host = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name="gamer_events")
    game = models.ForeignKey("Game", on_delete = models.CASCADE, related_name = "gamer_games")
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
