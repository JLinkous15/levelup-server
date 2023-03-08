from django.db import models


class Game(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    game_type = models.ForeignKey(
        "GameType", on_delete=models.CASCADE, related_name="GameType_Games")
    creator = models.CharField(max_length=50)
    number_of_players = models.IntegerField(default=1)
    skill_level = models.CharField(default="Easy", max_length=8)
    gamer = models.ForeignKey(
        "Gamer", on_delete=models.CASCADE, related_name="games")

    @property
    def is_host(self):
        return self.__host

    @is_host.setter
    def is_host(self, value):
        self.__host = value
