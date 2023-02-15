from django.db import models


class Event(models.Model):

    host = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name="host")
    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name = "event_games")
    attendance = models.ManyToManyField("Gamer", through="Attendance")
    date = models.DateTimeField()
    location = models.CharField(max_length=100)
