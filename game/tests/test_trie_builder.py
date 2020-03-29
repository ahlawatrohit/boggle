from django.test import TestCase
from game.trie_builder import TrieBuilder

class TestTrieBuilder(TestCase):

    def test_build_english_words_trie_from_empty_list(self):
        english_words_list = []
        expected_trie = {'valid': False}
        trie = TrieBuilder.build_english_words_trie(english_words_list)
        self.assertEqual(expected_trie, trie)

    def test_build_english_words_trie_from_list_of_empty_word(self):
        english_words_list = ['']
        expected_trie = {'valid': False}
        trie = TrieBuilder.build_english_words_trie(english_words_list)
        self.assertEqual(expected_trie, trie)

    def test_build_english_words_trie_one_letter_words(self):
        english_words_list = ['a', 'c', 'b', 'A']
        expected_trie = {
            'valid' : False,
            'a': {'valid': True},
            'b': {'valid': True},
            'c': {'valid': True}
        }

    def test_build_english_words_trie_two_letter_words(self):
        english_words_list = ['a', 'aa', 'b', 'bb', 'Aa']
        expected_trie = {
            'valid' : False,
            'a': {
                'valid': True,
                'a': {'valid': True}
            },
            'b': {
                'valid': True,
                'b': {'valid': True}
            }
        }

    def test_build_english_words_trie(self):
        english_words_list = ['app', 'ace', 'bin', 'bind', 'cats', 'cat', 'o']
        expected_trie = {
            'valid' : False,
            'a': {
                'valid': False,
                'p': {
                    'valid': False,
                    'p': {'valid': True}
                    },
                'c': {
                    'valid': False,
                    'e': {'valid': True}
                    }
                },
            'b': {
                'valid': False,
                'i': {
                    'valid': False,
                    'n': {
                        'valid': True,
                        'd': {'valid': True}
                        }
                    }
                },
            'c': {
                'valid': False,
                'a': {
                    'valid': False,
                    't': {
                        'valid': True,
                        's': {'valid': True}
                        }
                    }
                },
            'o': {'valid': True}
        }

        trie = TrieBuilder.build_english_words_trie(english_words_list)
        self.assertEqual(expected_trie, trie)

    def test_word_exists_in_empty_trie(self):
        english_words_list = []
        trie = TrieBuilder.build_english_words_trie(english_words_list)
        test_word_list = ['', 'a']
        for word in test_word_list:
            self.assertFalse(TrieBuilder.exists(word, trie))

    def test_word_exists_in_one_letter_trie(self):
        english_words_list = ['a', 'c', 'b']
        trie = TrieBuilder.build_english_words_trie(english_words_list)
        test_word_list = ['', 'aa', 'd']
        for word in test_word_list:
            self.assertFalse(TrieBuilder.exists(word, trie))
        test_word_list = english_words_list
        for word in test_word_list:
            self.assertTrue(TrieBuilder.exists(word, trie))

    def test_word_exists_in_two_letter_trie(self):
        english_words_list = ['a', 'aa', 'b', 'bb']
        trie = TrieBuilder.build_english_words_trie(english_words_list)
        test_word_list = ['', 'c', 'aaa']
        for word in test_word_list:
            self.assertFalse(TrieBuilder.exists(word, trie))
        test_word_list = english_words_list
        for word in test_word_list:
            self.assertTrue(TrieBuilder.exists(word, trie))

    def test_word_exists_in_trie(self):
        english_words_list = ['app', 'ace', 'bin', 'bind', 'cats', 'cat', 'o']
        trie = TrieBuilder.build_english_words_trie(english_words_list)
        test_word_list = ['', 'a', 'ac', 'tac']
        for word in test_word_list:
            self.assertFalse(TrieBuilder.exists(word, trie))
        test_word_list = english_words_list
        for word in test_word_list:
            self.assertTrue(TrieBuilder.exists(word, trie))

    def test_get_valid_words_list_from_empty_trie(self):
        english_words_list = []
        trie = TrieBuilder.build_english_words_trie(english_words_list)
        self.assertEqual(
            english_words_list,
            TrieBuilder.get_valid_words_list(trie)
        )

    def test_get_valid_words_list_from_one_letter_trie(self):
        english_words_list = ['a', 'c', 'b']
        trie = TrieBuilder.build_english_words_trie(english_words_list)
        self.assertEqual(
            english_words_list,
            TrieBuilder.get_valid_words_list(trie)
        )

    def test_get_valid_words_list_from_two_letter_trie(self):
        english_words_list = ['a', 'aa', 'b', 'bb']
        trie = TrieBuilder.build_english_words_trie(english_words_list)
        self.assertEqual(
            english_words_list,
            TrieBuilder.get_valid_words_list(trie)
        )

    def test_get_valid_words_list_from_trie(self):
        english_words_list = ['app', 'ace', 'bin', 'bind', 'cats', 'cat', 'o']
        trie = TrieBuilder.build_english_words_trie(english_words_list)
        expected_words_list = ['app', 'ace', 'bin', 'bind', 'cat', 'cats', 'o']
        self.assertEqual(
            expected_words_list,
            TrieBuilder.get_valid_words_list(trie)
        )
