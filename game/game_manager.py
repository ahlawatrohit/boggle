from .game import Game
from .boggle_cache import BoggleCache

class GameManager:
    INVALID = "invalid"
    VALID = "valid"
    ERROR_WORD_TOO_SHORT = "Word entered is too short"
    ERROR_NOT_VALID_WORD = "Not a valid word"
    ERROR_NO_GAME_FOUND = "No such game found"
    ERROR_WORD_ALREADY_GUESSED = "Word already guessed"
    MESSAGE_VALID_WORD = "Awesome!!!"

    #
    # Load the english words dictionary on application startup. This dictionary
    # (loaded in a trie) contains the list of valid english word from the nltk
    # library.
    #
    @classmethod
    def load_english_dictionary(cls):
        BoggleCache.load_english_dictionary()

    #
    # Create a new game
    #
    @classmethod
    def create_new_game(cls):
        game = Game()
        game.create_game(BoggleCache.get_english_word_trie_root())
        BoggleCache.gameid_to_game_cache[game.game_id] = game
        return game.get_game_response()

    #
    # Get list of game words for a given game id
    #
    @classmethod
    def get_game_words(cls, game_id):
        list = []
        if game_id in BoggleCache.gameid_to_game_cache:
            game = BoggleCache.gameid_to_game_cache.get(game_id)
            list = game.get_game_words_list()
        response = {}
        response['result'] = list
        return response

    #
    # Rotate the game grid for a given game id
    #
    @classmethod
    def rotate_game_grid(cls, game_id):
        response = {}
        if game_id in BoggleCache.gameid_to_game_cache:
            game = BoggleCache.gameid_to_game_cache.get(game_id)
            response['grid'] = game.rotate_game_grid()
        return response
    #
    # Validate if the given word for a gameid is a valid word
    #
    @classmethod
    def check_word(cls, game_id, word):
        if game_id in BoggleCache.gameid_to_game_cache:
            game = BoggleCache.gameid_to_game_cache.get(game_id)
            word_length = len(word)
            if word_length < game.acceptable_min_word_length:
                return cls.build_response(
                    cls.INVALID,
                    cls.ERROR_WORD_TOO_SHORT,
                    0
                )
            already_guessed = game.is_word_already_guessed(word)
            if bool(already_guessed) == True:
                return cls.build_response(
                    cls.INVALID,
                    cls.ERROR_WORD_ALREADY_GUESSED,
                    0
                )
            exists = game.is_valid_word(word)
            if bool(exists) == True:
                return cls.build_response(
                    cls.VALID,
                    cls.MESSAGE_VALID_WORD,
                    len(word)
                )
            else:
                return cls.build_response(
                    cls.INVALID,
                    cls.ERROR_NOT_VALID_WORD,
                    0
                )
        return cls.build_response(cls.INVALID, cls.ERROR_NO_GAME_FOUND, 0)

    #
    # Build response for validation based on current game state
    #
    @classmethod
    def build_response(cls, status, message,score):
        response = {}
        response['status'] = status
        response['message'] = message
        response['score'] = score
        return response
