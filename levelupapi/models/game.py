from django.db import models

class Game(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE, related_name="GameType_Games")
    creator = models.CharField(max_length=50)
    number_of_players = models.IntegerField(default=1)
    skill_level = models.CharField(default="Easy", max_length=8)