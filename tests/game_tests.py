import json
from rest_framework import status
from rest_framework.test import APITestCase
from levelupapi.models import GameType, Gamer, Game
from rest_framework.authtoken.models import Token


class GameTests(APITestCase):

    # Add any fixtures you want to run to build the test database
    fixtures = ['users', 'tokens', 'gamers', 'game_types', 'games', 'events']

    def setUp(self):
        self.gamer = Gamer.objects.first()
        token = Token.objects.get(user=self.gamer.user)
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")

    def test_create_game(self):
        """
        Ensure we can create a new game.
        """
        # Define the endpoint in the API to which
        # the request will be sent
        url = "/games"

        # Define the request body
        data = {
            "game_type": 1,
            "skill_level": "Easy",
            "name": "Clue",
            "creator": "Milton Bradley",
            "number_of_players": 6,
            "description": "Fun for the whole family",
        }

        # Initiate request and store response
        response = self.client.post(url, data, format='json')

        # Parse the JSON in the response body
        json_response = json.loads(response.content)

        # Assert that the game was created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the properties on the created resource are correct
        self.assertEqual(json_response["name"], "Clue")
        self.assertEqual(json_response["creator"], "Milton Bradley")
        self.assertEqual(json_response["skill_level"], "Easy")
        self.assertEqual(json_response["number_of_players"], 6)
        self.assertEqual(
            json_response["description"], "Fun for the whole family")
        self.assertEqual(
            json_response["game_type"], 1)

    def test_change_game(self):
        """
        Ensure we can change an existing game.
        """
        game_type = GameType(pk=2)
        game = Game()
        game.game_type = game_type
        game.skill_level = "Easy"
        game.name = "Not Sorry"
        game.creator = "Milton Brandon"
        game.number_of_players = 6
        game.description = "Look at this description."
        game.save()

        # DEFINE NEW PROPERTIES FOR GAME
        data = {
            "game_type": 1,
            "skill_level": "Hard",
            "name": "Sorry",
            "creator": "Hasbro",
            "number_of_players": 4,
            "description": "Look at that description!"
        }

        response = self.client.put(f"/games/{game.id}", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET game again to verify changes were made
        response = self.client.get(f"/games/{game.id}")
        json_response = json.loads(response.content)

        # Assert that the properties are correct
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json_response["name"], "Sorry")
        self.assertEqual(json_response["creator"], "Hasbro")
        self.assertEqual(json_response["skill_level"], "Hard")
        self.assertEqual(json_response["number_of_players"], 4)
        self.assertEqual(
            json_response["description"], "Look at that description!")

    def test_delete_game(self):
        """
        Ensure we can delete an existing game.
        """
        game_type = GameType(pk=1)
        game = Game()
        game.game_type = game_type
        game.skill_level = "Medium"
        game.name = "Sorry"
        game.creator = "Milton Bradley"
        game.number_of_players = 4
        game.save()

        # self.client.post
        # DELETE the game you just created
        response = self.client.delete(f"/games/{game.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET the game again to verify you get a 404 response
        response = self.client.get(f"/games/{game.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
