import json
from rest_framework import status
from rest_framework.test import APITestCase
from levelupapi.models import GameType, Gamer, Game, Event
from rest_framework.authtoken.models import Token


class EventTests(APITestCase):

    fixtures = ['users', 'tokens', 'gamers', 'events', 'games', 'game_types']

    def setUp(self):
        self.gamer = Gamer.objects.first()
        token = Token.objects.get(user=self.gamer.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

    def test_signup_and_leave_action(self):
        """
        Testing Gamer instances can be added to Event.attendees per the signup custom action
        """
        event = Event.objects.first()
        gamer = Gamer.objects.first()
        url1 = f'/events/{event.pk}/signup'
        url2 = f'/events/{event.pk}/leave'

        response = self.client.post(url1, None, format='json')
        json_response = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response["message"], "Gamer added")

        # certain assert method pytest assertion value in array

        response = self.client.get(f'/events/{event.pk}')
        gamer_response = self.client.get(f'/gamers/{gamer.pk}')
        json_response = json.loads(response.content)
        json_gamer = json.loads(gamer_response.content)
        self.assertEqual(response.status_code,
                         status.HTTP_200_OK, msg="Not a 200 status code")
        self.assertIn(
            json_gamer, json_response["attendance"], msg="data is not found in attendance list")

        response = self.client.delete(url2)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertNotIn(
            json_gamer, json_response["attendance"], msg="data is not found in attendance list")
