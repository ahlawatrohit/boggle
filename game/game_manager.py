from .game import Game
from .boggle_cache import BoggleCache

class GameManager:

    #
    # Load the english words dictionary on application startup. This dictionary
    # (loaded in a trie) contains the list of valid english word from the nltk
    # library.
    #
    @classmethod
    def load_english_dictionary(cls):
        BoggleCache.load_english_dictionary()
        print("Boggle Cache initalized")

    @classmethod
    def create_new_game(cls):
        game = Game()
        game.create_game_board()
        game.create_game_words()
        #add to cache -> get a trie and write to cache
        BoggleCache.generate_game_words_trie(
            game.grid,
            game.row,
            game.column,
            game.game_id
            )
        return game.get_game_response()
