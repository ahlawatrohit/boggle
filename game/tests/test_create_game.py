from django.test import TestCase
from game.boggle_cache import BoggleCache
from game.game import Game
from game.trie_builder import TrieBuilder

class TestCreateGame(TestCase):

    def test_create_game_all_same_letters(self):
        game = Game()
        game.grid = 'EEEEEEEEEEEEEEEE'
        self.assertEqual(16, len(game.grid))
        game._create_valid_game_words(BoggleCache.english_words_trie_root)
        test_words_list = ['e']
        for word in test_words_list:
            self.assertTrue(TrieBuilder.exists(word, game.valid_words_trie))
        test_words_list = ['ee', 'eee', 'eeee', '']
        for word in test_words_list:
            self.assertFalse(TrieBuilder.exists(word, game.valid_words_trie))

    def test_create_game(self):
        game = Game()
        game.grid = 'ETLHASHSBVQEAAYT'
        self.assertEqual(16, len(game.grid))
        game._create_valid_game_words(BoggleCache.english_words_trie_root)
        test_words_list = ['sea', 'stab', 'she', 'hey', 'yes', 'ava', 'se', 'set', 'sey']
        for word in test_words_list:
            self.assertTrue(TrieBuilder.exists(word, game.valid_words_trie))
        test_words_list = ['av', 'avs', 'eas', 'heq', '']
        for word in test_words_list:
            self.assertFalse(TrieBuilder.exists(word, game.valid_words_trie))

    def test_game_words_list_all_same_letters(self):
        game = Game()
        game.grid = 'EEEEEEEEEEEEEEEE'
        game._create_valid_game_words(BoggleCache.english_words_trie_root)

        #
        # game_words_list returns all valid words of
        # length >= acceptable_min_word_length
        #
        expected_words_list = []
        self.assertEqual(expected_words_list, game.get_game_words_list())

    def test_game_words_list_all_same_letters(self):
        game = Game()
        game.grid = 'ETLHASHSBVQEAAYT'
        game._create_valid_game_words(BoggleCache.english_words_trie_root)

        expected_words_list = ['eta', 'eat', 'eats', 'east', 'esth', 'tea',
            'tae', 'tash', 'tab', 'tav', 'tavy', 'the', 'they', 'tye', 'hey',
            'het', 'aes', 'ate', 'ates', 'ase', 'ast', 'ash', 'ashes', 'ashet',
            'aba', 'abate', 'abas', 'abase', 'abash', 'ava', 'avast', 'aye',
            'set', 'seta', 'seth', 'sea', 'seat', 'seathe', 'seavy', 'sey',
            'stab', 'sat', 'sate', 'sab', 'saba', 'she', 'bae', 'bat', 'bate',
            'bats', 'bath', 'bathe', 'bas', 'base', 'bast', 'baste', 'bash',
            'baa', 'bay', 'vat', 'vas', 'vase', 'vast', 'yes', 'yet', 'yaba',
            'yava']
        self.assertEqual(expected_words_list, game.get_game_words_list())
