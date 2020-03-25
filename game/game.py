from datetime import datetime
from .boggle_cache import BoggleCache
from .trie_builder import TrieBuilder
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

    VALID_DIRECTIONS = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
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
        for entry in Game.CELLS:
            self.grid = self.grid +  entry[random.randrange(0, 6)]

    #
    # Creates the valid words which can be made from the input grid
    # and stores it in a trie datastructure as part of Game object
    #
    def create_valid_game_words(self):
        print('create_game_words')
        word_list = []
        self._game_words_trie(BoggleCache.english_words_trie_root, word_list)
        game_trie = TrieBuilder.build_english_words_trie(word_list)
        self.valid_words = game_trie


    def create_game(self):
        self.create_game_board()
        self.create_valid_game_words()

    #
    # Creates Game lite object which would be returned to the user
    #
    def get_game_response(self):
        response = {}
        response['game_id'] = self.game_id
        response['row'] = self.row
        response['column'] = self.column
        response['grid'] = self.grid
        response['timestamp'] = self.timestamp

        return response

    #
    # Create a matrix of input string and perform depth first search
    # on it to find all the valid words by comparing to english trienode
    # that we have in memory
    #
    def _game_words_trie(self,english_trie,game_words_list):
        length = len(self.grid)
        board = [[0 for j in range(self.column) ]
            for i in range(self.row)]
        index = 0
        grid = self.grid.lower()
        for i in range(self.row) :
            for j in range(self.column) :
                board[i][j] = grid[index]
                index +=1
        for row in range(self.row):
            for column in range(self.column) :
                letter = board[row][column]
                self._traverse_grid(row,column,[],'',board,english_trie,game_words_list)

    #
    # Recursively use dfs to populate valid word list for the game
    #
    def _traverse_grid(
        self,
        row,
        column,
        visited,
        now_word,
        board,
        english_trie,
        game_words_list
        ):
        if (row, column) in visited:
            return
        letter = board[row][column]
        visited.append((row, column))

        if letter in english_trie:
            now_word += letter

            if english_trie[letter]['valid']:
                print(now_word)
                game_words_list.append(now_word)

            neighbors = self._get_valid_directions(row,column)
            for dir in neighbors:
                self._traverse_grid(dir[0],
                        dir[1],
                        visited[::],
                        now_word,
                        board,
                        english_trie[letter],
                        game_words_list
                    )

    #
    #  Returns valid directions on the board for a given cell
    #
    def _get_valid_directions(self, row, column):
        neighbors = []
        for pos in self.VALID_DIRECTIONS:
            new_row = row + pos[0]
            new_column = column + pos[1]

            if ((new_row >= self.row) or
                (new_column >= self.column) or
                (new_row < 0) or
                (new_column < 0)):
                continue
            neighbors.append((new_row, new_column))
        return neighbors
