from .gameutil import GameUtil
from datetime import datetime
import uuid

class Game:
    board_row = 4               #defining game grid row size as 4
    board_column = 4            #defining game grid column size as 4
    min_length_valid_word = 3   #defining minimum valid word size as 3
    gameutil = GameUtil()

    #
    # When the user starts a new game, the board is loaded and returned
    # Every new game generates a unique visitor id and game id
    #
    def start(self):
        env={}
        env['vi'] = str(uuid.uuid4())
        env['gameId'] = str(uuid.uuid4())
        env['row'] =  self.board_row
        env['column'] = self.board_column
        env['grid'] = self.gameutil.generate_grid()
        env['timestamp'] = datetime.now()
        return env
