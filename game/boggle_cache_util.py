class BoggleCacheUtil:
    valid_directions = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1),
    ]

    #
    # build and return the trie of valid english words from words list
    #
    def build_english_word_trie(self, words, trienode):
        for word in words:
            self.generate_english_word_trie(word, trienode)
        return trienode

    #
    # recursively populate the words in trie
    #
    def generate_english_word_trie(self, word, trienode):
        if not word:
            return
        if word[0] not in trienode:
            trienode[word[0]] = {'valid': len(word) == 1, 'next': {}}
        # recursively build trienode
        self.generate_english_word_trie(word[1:], trienode[word[0]])

    #
    # create a matrix of input string and perform deapth first search
    # on it to find all the valid words by comparing to english trienode
    # that we have in memory
    #
    def game_words_trie(self,
                        grid,
                        board_row,
                        board_column,
                        english_trie,
                        game_words_list
                       ):
        length = len(grid)
        board = [[0 for j in range(board_column) ]
            for i in range(board_row)]
        index = 0
        for i in range(board_row) :
            for j in range(board_column) :
                board[i][j] = grid[index]
                index +=1
        for row in range(board_row):
            for column in range(board_column) :
                letter = board[row][column]
                self.dfs(row,
                         column,
                         [],
                         '',
                         board,
                         board_row,
                         board_column,
                         english_trie,
                         game_words_list)

    #
    # recursively use dfs to populate valid word list for the game
    #
    def dfs(
        self,
        row,
        column,
        visited,
        now_word,
        board,
        board_row,
        board_column,
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

            neighbors = self.get_valid_directions(
                row,
                column,
                board_row,
                board_column
            )
            for dir in neighbors:
                self.dfs(
                        dir[0],
                        dir[1],
                        visited[::],
                        now_word,
                        board,
                        board_row,
                        board_column,
                        english_trie[letter],
                        game_words_list
                    )

    #
    #  returns valid directions on the board for a given cell
    #
    def get_valid_directions(self, row, column, board_row, board_column):
        neighbors = []
        for pos in self.valid_directions:
            new_row = row + pos[0]
            new_column = column + pos[1]

            if ((new_row >= board_row) or
                (new_column >= board_column) or
                (new_row < 0) or
                (new_column < 0)):
                continue
            neighbors.append((new_row, new_column))
        return neighbors
