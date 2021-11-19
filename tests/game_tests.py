from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from gamer_rater_api.models import GameRating, Game
from gamer_rater_api.models.category import Category

class GameTests(APITestCase):
    def setUp(self):
        """
        Create a new Gamer, collect the auth Token, and create a sample GameType
        """

        # Define the URL path for registering a Gamer
        url = '/register'

        # Define the Gamer properties
        player = {
            "username": "steve",
            "password": "Admin8*",
            "email": "steve@stevebrownlee.com",
            "address": "100 Infinity Way",
            "phone_number": "555-1212",
            "first_name": "Steve",
            "last_name": "Brownlee",
            "name": "DeathBoi"
        }

        # Initiate POST request and capture the response
        response = self.client.post(url, player, format='json')

        # Store the TOKEN from the response data
        self.token = Token.objects.get(pk=response.data['token'])

        # Use the TOKEN to authenticate the requests
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Assert that the response status code is 201 (CREATED)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # SEED THE DATABASE WITH A GAMETYPE
        # This is necessary because the API does not
        # expose a /gametypes URL path for creating GameTypes
        category = Category()
        category.label = "Board game"

        # Save the GameType to the testing database
        category.save()


    def test_create_game(self):
        """
        Ensure we can create (POST) a new Game.
        """

        # Define the URL path for creating a new Game
        url = "/games"

        # Define the Game properties
        game = {
            "title": "Clue",
            "designer": "Milton Bradley",
            "yearReleased": 1949,
            "playTime": "6.90",
            "ageRecommendation": 6,
            "categoryId": 1,
        }

        # Initiate POST request and capture the response
        response = self.client.post(url, game, format='json')

        # Assert that the response status code is 201 (CREATED)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the values are correct
        self.assertEqual(response.data["title"], game['title'])
        self.assertEqual(response.data["designer"], game['designer'])
        self.assertEqual(response.data["play_time"], game['playTime'])
        self.assertEqual(response.data["age_recommendation"], game['ageRecommendation'])
        self.assertEqual(len(response.data["categories"]), 1)

    def test_change_game(self):
        """
        Ensure we can change an existing game.
        """

        # Create a new instance of Game
        game = Game()
        game.play_time = 5
        game.title = "Sorry"
        game.designer = "Milton Bradley"
        game.age_recommendation = 4
        game.categories = [1,2]

        # Save the Game to the testing database
        game.save()

        # Define the URL path for updating an existing Game
        url = f'/games/{game.id}'

        # Define NEW Game properties
        new_game = {
            "title": "Sorry",
            "designer": "Hasbro",
            "yearRealease": 1958,
            "playTime": 2,
            "ageRecommendation": 4,
            "categoryIds": [1,2]
        }

        # Initiate PUT request and capture the response
        response = self.client.put(url, new_game, format="json")

        # Assert that the response status code is 204 (NO CONTENT)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Initiate GET request and capture the response
        response = self.client.get(url)

        # Assert that the response status code is 200 (OK)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the values are correct
        self.assertEqual(response.data["gamer"]['id'], self.token.user_id)
        self.assertEqual(response.data["title"], new_game['title'])
        self.assertEqual(response.data["designer"], new_game['designer'])
        self.assertEqual(
            response.data["year_released"], new_game['yearReleased'])
        self.assertEqual(
            response.data["age_recommendation"], new_game['ageRecommendation'])
        self.assertEqual(response.data["categories"]['id'], new_game['categoryId'])

    # def test_get_game(self):
    #     """
    #     Ensure we can GET an existing game.
    #     """

    #     # Create a new instance of Game
    #     game = Game()
    #     game.gamer_id = 1
    #     game.title = "Monopoly"
    #     game.designer = "Milton Bradley"
    #     game.skill_level = 5
    #     game.age_recommendation = 4
    #     game.categoryIds =[1,2]

    #     # Save the Game to the testing database
    #     game.save()

    #     # Define the URL path for getting a single Game
    #     url = f'/games/{game.id}'

    #     # Initiate GET request and capture the response
    #     response = self.client.get(url)

    #     # Assert that the response status code is 200 (OK)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    #     # Assert that the values are correct
    #     self.assertEqual(response.data["gamer"]['id'], game.categories)
    #     self.assertEqual(response.data["title"], game.title)
    #     self.assertEqual(response.data["designer"], game.designer)
    #     self.assertEqual(response.data["skill_level"], game.skill_level)
    #     self.assertEqual(response.data["age_recommendation"], game.age_recommendation)
    #     self.assertEqual(response.data["categories"]['id'], game.categories_id)

    # def test_delete_game(self):
    #     """
    #     Ensure we can delete an existing game.
    #     """

    #     # Create a new instance of Game
    #     game = Game()
    #     game.categories = 1
    #     game.title = "Sorry"
    #     game.designer = "Milton Bradley"
    #     game.skill_level = 5
    #     game.age_recommendation = 4
    #     game.categories_id = 1
    #     game.description = "It's too late to apologize."

    #     # Save the Game to the testing database
    #     game.save()

    #     # Define the URL path for deleting an existing Game
    #     url = f'/games/{game.id}'

    #     # Initiate DELETE request and capture the response
    #     response = self.client.delete(url)

    #     # Assert that the response status code is 204 (NO CONTENT)
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    #     # Initiate GET request and capture the response
    #     response = self.client.get(url)

    #     # Assert that the response status code is 404 (NOT FOUND)
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
