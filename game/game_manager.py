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
        game.create_game()
        BoggleCache.gameid_to_game_cache[game.game_id] = game
        return game.get_game_response()
