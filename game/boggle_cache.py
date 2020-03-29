from nltk.corpus import words
from .trie_builder import TrieBuilder

class BoggleCache:
    english_words_list = words.words()
    english_words_trie_root = {'valid': False}
    gameid_to_game_cache = {}

    #
    # Load the english words dictionary on application startup. This dictionary
    # (loaded in a trie) contains the list of valid english word from the nltk
    # library.
    #
    @classmethod
    def load_english_dictionary(cls):
        cls.english_words_trie_root = TrieBuilder.build_english_words_trie(
            cls.english_words_list
        )

    #
    # Get english dictionary trie node
    #
    @classmethod
    def get_english_word_trie_root(cls):
        return cls.english_words_trie_root
