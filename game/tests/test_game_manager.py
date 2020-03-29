from django.test import TestCase
from game.game_manager import GameManager

class TestGameManager(TestCase):

    def test_boggle(self):
        response_new_game = GameManager.create_new_game()
        gameid = response_new_game['game_id']
        response_game_valid_words = GameManager.get_game_words(gameid)
        for word in response_game_valid_words['result']:
            response = GameManager.check_word(gameid, word)
            self.assertEqual(GameManager.VALID, response['status'])

        #
        # Already checked words are saved in cache and are invalid if checked
        # again
        #
        for word in response_game_valid_words['result']:
            response = GameManager.check_word(gameid, word)
            self.assertEqual(GameManager.INVALID, response['status'])

    def test_boggle_with_rotate(self):
        response_new_game = GameManager.create_new_game()
        gameid = response_new_game['game_id']
        response_game_valid_words = GameManager.get_game_words(gameid)
        GameManager.rotate_game_grid(gameid)
        for word in response_game_valid_words['result']:
            response = GameManager.check_word(gameid, word)
            self.assertEqual(GameManager.VALID, response['status'])
