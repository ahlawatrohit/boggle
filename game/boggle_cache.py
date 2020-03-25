from nltk.corpus import words
from .boggle_cache_util import BoggleCacheUtil

class BoggleCache:
    english_word_list = words.words()
    english_word_trie_node = {'valid': False, 'next': {}}
    game_valid_words_trie = {}
    boggle_cache_util = BoggleCacheUtil()

    #
    # Load the english words dictionary on application startup. This dictionary
    # (loaded in a trie) contains the list of valid english word from the nltk
    # library.
    #
    @classmethod
    def load_english_dictionary(cls):
        cls.english_word_trie_node = cls.boggle_cache_util.build_english_word_trie(
            cls.english_word_list,
            cls.english_word_trie_node
        )
        print("Boggle Cache initalized")

    #
    # every game will have a trie in memory which will contain
    # valid words that can be formed using the grid
    #
    @classmethod
    def generate_game_words_trie(cls, grid, board_row, board_column, game_id):
        game_trie = {'valid': False, 'next': {}}
        word_list = []
        cls.boggle_cache_util.game_words_trie(
            grid.lower(),
            board_row, board_column,
            cls.english_word_trie_node,
            word_list
            )
        game_trie = cls.boggle_cache_util.build_english_word_trie(
            word_list, game_trie
            )
        cls.game_valid_words_trie[game_id] = game_trie
