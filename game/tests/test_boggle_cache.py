from django.test import TestCase
from game.boggle_cache import BoggleCache
from nltk.corpus import words

class TestBoggleCache(TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    def test_load_empty_english_dictionary(self):
        BoggleCache.english_words_list = []
        BoggleCache.load_english_dictionary()
        expected_trie = {'valid': False}
        self.assertEqual(
            expected_trie,
            BoggleCache.get_english_word_trie_root()
        )

    def test_load_one_letter_words_english_dictionary(self):
        BoggleCache.english_words_list = ['a', 'c', 'b', 'A']
        BoggleCache.load_english_dictionary()
        expected_trie = {
            'valid' : False,
            'a': {'valid': True},
            'b': {'valid': True},
            'c': {'valid': True}
        }
        self.assertEqual(
            expected_trie,
            BoggleCache.get_english_word_trie_root()
        )

    def test_load_two_letter_words_english_dictionary(self):
        BoggleCache.english_words_list = ['a', 'aa', 'b', 'bb', 'Aa']
        BoggleCache.load_english_dictionary()
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
        self.assertEqual(
            expected_trie,
            BoggleCache.get_english_word_trie_root()
        )

    def test_load_english_dictionary(self):
        BoggleCache.english_words_list = ['app', 'ace', 'bin', 'bind', 'cats', 'cat', 'o']
        BoggleCache.load_english_dictionary()
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
        self.assertEqual(
            expected_trie,
            BoggleCache.get_english_word_trie_root()
        )

    @classmethod
    def tearDownClass(cls):
        #
        # Reset back to the original english word dictionary for the other
        # tests
        #
        BoggleCache.english_words_list = words.words()
        BoggleCache.load_english_dictionary()
