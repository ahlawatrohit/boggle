from datetime import datetime
import random
import uuid

class Game:

    #
    # Every cell of the 4 by 4 game grid would have one character
    # randomly chosen from this set
    #
    CELLS = [
        "NEEHGW",
        "TMIOUC",
        "YTLETR",
        "NLNHRZ",
        "WTOOAT",
        "IUNEES",
        "HSPACO",
        "SSOIET",
        "BAOBOJ",
        "RYVDEL",
        "QUMHNI",
        "IERLDX",
        "NEEGAA",
        "FPSAKF",
        "STITYP",
        "WRETVH"
    ]

    def __init__(self):
        self.game_id = str(uuid.uuid4())
        self.row = 4
        self.column = 4
        self.grid = ''
        self.acceptable_min_word_length = 3
        self.timestamp = str(datetime.now())

    #
    # Generate game grid with random characters from the above cells list
    #
    def create_game_board(self):
        grid = ""
        for entry in Game.CELLS:
            grid = grid +  entry[random.randrange(0,6)]
        self.grid = grid

    #
    # Creates the valid words which can be made from the input grid
    # and stores it in a trie datastructure as part of Game object
    #
    def create_game_words(self):
        print('create_game_words')

    #
    # Creates Game lite object which would be returned to the user
    #
    def get_game_response(self):
        game = {}
        game['game_id'] = self.game_id
        game['row'] = self.row
        game['column'] = self.column
        game['grid'] = self.grid
        game['timestamp'] = self.timestamp

        return game
