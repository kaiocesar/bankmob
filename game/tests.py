from django.test import TestCase
from game.models import Player
from django.contrib.auth.models import User

class PlayerTestCase(TestCase):
    def setUp(self):
        fulaninho = User.objects.create(
            username='fulaninho@email.com', 
            email='fulaninho@email.com', 
            password='123123123')

        Player.objects.create(
            user = fulaninho,
            points = 10,
            steps = 1
        )


    def test_add_player_the_game(self):
        players = Player.objects.all()
        self.assertEqual(len(players), 2)

