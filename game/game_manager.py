from .game import Game
from .boggle_cache import BoggleCache

class GameManager:
    INVALID = "invalid"
    VALID = "valid"
    ERROR_WORD_TOO_SHORT = "Word entered is too short"
    ERROR_NOT_VALID_WORD = "Not a valid word"
    ERROR_NO_GAME_FOUND = "No such game found"
    MESSAGE_VALID_WORD = "Awesome!!!"
    #
    # Load the english words dictionary on application startup. This dictionary
    # (loaded in a trie) contains the list of valid english word from the nltk
    # library.
    #
    @classmethod
    def load_english_dictionary(cls):
        BoggleCache.load_english_dictionary()
        print("Boggle Cache initalized")

    #
    # Create a new game
    #
    @classmethod
    def create_new_game(cls):
        game = Game()
        game.create_game()
        print("writing to game_id" + game.game_id)
        BoggleCache.gameid_to_game_cache[game.game_id] = game
        return game.get_game_response()

    #
    # Validate if the given word for a gameid is a valid word
    #
    @classmethod
    def check_word(cls, game_id, word):
        response = {}
        if game_id in BoggleCache.gameid_to_game_cache:
            game = BoggleCache.gameid_to_game_cache.get(game_id)
            word_length = len(word)
            if word_length < game.acceptable_min_word_length:
                response['status'] = cls.INVALID
                response['message'] = cls.ERROR_WORD_TOO_SHORT
                return response
            exists = game.is_valid_word(word)
            if bool(exists) == True:
                response['status'] = cls.VALID
                response['message'] = cls.MESSAGE_VALID_WORD
                return response
            else:
                response['status'] = cls.INVALID
                response['message'] = cls.ERROR_NOT_VALID_WORD
                return response
        response['status'] = cls.INVALID
        response['message'] = cls.ERROR_NO_GAME_FOUND
        return response;
