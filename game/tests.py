from django.test import TestCase
from game.models import Player
from django.contrib.auth.models import User

class PlayerTestCase(TestCase):
    def setUp(self):
        self.fulaninho = User.objects.create(
            username='fulaninho@email.com', 
            email='fulaninho@email.com', 
            password='123123123')

        Player.objects.create(
            user = self.fulaninho,
            points = 10,
            steps = 1
        )

    def test_get_player(self):
        players = Player.objects.all()
        self.assertEqual(len(players), 1)

    def test_creating_new_player_with_default_values(self):
        player_1 = Player.objects.create(
            user = self.fulaninho
        )
        self.assertEqual(player_1.user.username, 'fulaninho@email.com')
        self.assertEqual(player_1.points, 300)
        self.assertEqual(player_1.steps, 0)