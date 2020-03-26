class TrieBuilder:

    #
    # Build and return the trie of valid english words from words list
    #
    @classmethod
    def build_english_words_trie(cls, words):
        trie_node = {'valid': False, 'next': {}}
        for word in words:
            cls._generate_english_word_trie(word, trie_node)
        return trie_node

    #
    # Recursively populate the words in trie
    #
    @classmethod
    def _generate_english_word_trie(cls, word, trie_node):
        if not word:
            return
        if word[0] not in trie_node:
            trie_node[word[0]] = {'valid': len(word) == 1, 'next': {}}
        # recursively build trienode
        cls._generate_english_word_trie(word[1:], trie_node[word[0]])

    #
    # Returns true if the given word exists in the given trie
    #
    @classmethod
    def exists(cls, word, trie_node):
        if not word:
            return True
        if word[0] not in trie_node:
            return False
        return cls.exists(word[1:], trie_node[word[0]])
