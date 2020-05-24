from django.test import TestCase
from django.test import Client
from .models import User, Player


class PlayerTestCase(TestCase):
    def setUp(self):
        self.client_http = Client()

        self.fulaninho = User.objects.create(
            username='fulaninho@email.com',
            email='fulaninho@email.com',
            password='123123123')

        Player.objects.create(
            user=self.fulaninho,
            points=10,
            steps=1
        )

    def test_get_player(self):
        players = Player.objects.all()
        self.assertEqual(len(players), 1)

    def test_creating_new_player_with_default_values(self):
        player_1 = Player.objects.create(
            user=self.fulaninho
        )
        self.assertEqual(player_1.user.username, 'fulaninho@email.com')
        self.assertEqual(player_1.points, 300)
        self.assertEqual(player_1.steps, 0)

    def test_request_add_player(self):
        response = self.client_http.post('/player', {'user_id': '123'})
        self.assertEqual(response.status_code, 200)

    # def test_request_start_the_game(self):
    #     response = self.client_http.get('/game/456')
    #     self.assertEqual(response.status_code, 200)

    # def test_request_roll_the_dice(self):
    #     response = self.client_http.post('/game', {'user_id': '123'})
    #     self.assertEqual(response.status_code, 200)

    # def test_buy_property(self):
    #     response = self.client_http.post('/property',
    #                   {'user_id': '123', 'buy': 'true'})
    #     self.assertEqual(response.status_code, 200)

    # def test_rent_property(self):
    #     response = self.client_http.post('/property',
    #                   {'user_id': '123', 'rent': 'true'})
    #     self.assertEqual(response.status_code, 200)
