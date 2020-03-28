class TrieBuilder:

    #
    # Build and return the trie of valid english words from words list
    #
    @classmethod
    def build_english_words_trie(cls, words):
        trie_node = {'valid': False}
        for word in words:
            cls._generate_english_word_trie(word.lower(), trie_node)
        return trie_node

    #
    # Recursively populate the words in trie
    #
    @classmethod
    def _generate_english_word_trie(cls, word, trie_node):
        if not word:
            return
        if word[0] not in trie_node:
            trie_node[word[0]] = {'valid': len(word) == 1}
        # recursively build trienode
        cls._generate_english_word_trie(word[1:], trie_node[word[0]])

    #
    # Returns true if the given word exists in the given trie
    #
    @classmethod
    def exists(cls, word, trie_node):
        if not word and trie_node['valid'] == True:
            return True
        if not word:
            return False
        if word[0] not in trie_node:
            return False
        return cls.exists(word[1:], trie_node[word[0]])

    #
    # Returns list of all the valid words stored in the given trie
    #
    @classmethod
    def get_valid_words_list(cls, trie_node):
        word_list = []
        if trie_node:
             for k,v in trie_node.items():
                 if str(k) != 'valid':
                     for item in cls.get_valid_words_list(v):
                         word_list.append(k + item)
                 else:
                     if bool(v) == True:
                         word_list.append('')
        return word_list
