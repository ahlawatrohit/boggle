from django.test import TestCase
from game.boggle_cache import BoggleCache
from game.game import Game
from game.trie_builder import TrieBuilder

class TestGame(TestCase):

    game = None

    @classmethod
    def setUpClass(cls):
        cls.game = Game()
        cls.game.grid = 'ETLHASHSBVQEAAYT'
        cls.game.create_game(BoggleCache.english_words_trie_root)

    def test_is_valid_word(self):
        test_words_list = ['sea', 'stab', 'she', 'hey', 'yes', 'ava', 'se', 'set', 'sey']
        for word in test_words_list:
            self.assertTrue(TestGame.game.is_valid_word(word))
        test_words_list = ['av', 'avs', 'eas', 'heq', '']
        for word in test_words_list:
            self.assertFalse(TestGame.game.is_valid_word(word))

    def test_is_word_already_guessed(self):
        test_words_list = ['sea', 'stab', 'she', 'hey', 'yes', 'ava', 'se', 'set', 'sey']
        for word in test_words_list:
            self.assertTrue(TestGame.game.is_valid_word(word))
        test_words_list = ['sea', 'stab', 'she', 'hey', 'yes', 'ava', 'se', 'set', 'sey']
        for word in test_words_list:
            self.assertTrue(TestGame.game.is_word_already_guessed(word))

    def test_rotate_words(self):
        test_valid_words_list = ['sea', 'stab', 'she', 'hey', 'yes', 'ava', 'se', 'set', 'sey']
        for word in test_valid_words_list:
            self.assertTrue(TestGame.game.is_valid_word(word))
        test_invalid_words_list = ['av', 'avs', 'eas', 'heq', '']
        for i in range(10):
            TestGame.game.rotate_game_grid()
            for word in test_valid_words_list:
                self.assertTrue(TestGame.game.is_valid_word(word))
            for word in test_invalid_words_list:
                self.assertFalse(TestGame.game.is_valid_word(word))

    @classmethod
    def tearDownClass(cls):
        pass
