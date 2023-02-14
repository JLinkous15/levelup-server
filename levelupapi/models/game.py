from django.db import models

class Game(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE, related_name="GameType_Games")
    creator = models.ForeignKey("Gamer", on_delete=models.CASCADE, related_name="creators_games")