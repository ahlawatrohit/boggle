from nltk.corpus import words

class BoggleCache:
    english_word_list = words.words()
    english_word_trie_node = {'valid': False, 'next': {}}

    #
    # load the english word trie at startup
    # this contains list of valid english word from nltk library
    #
    def load_trie_on_startup(self):
        BoggleCache.english_word_trie_node = self.build_english_word_trie(
            BoggleCache.english_word_list, BoggleCache.english_word_trie_node
            )
        print("Boggle Cache initalized")

    #
    # build the trie for the valid english word at startup
    #
    def build_english_word_trie(self,words, trienode):
        for word in words:
            self.generate_english_word_trie(word, trienode)
        return trienode

    #
    # recursively populate the words in trie
    #
    def generate_english_word_trie(self,word, node):
        if not word:
            return

        if word[0] not in node:
            node[word[0]] = {'valid': len(word) == 1, 'next': {}}

        # recursively build trie
        self.generate_english_word_trie(word[1:], node[word[0]])
