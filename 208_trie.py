class Trie:
    END_CHARACTER = '#'
    characters = dict()

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if len(word) == 0:
            self.characters = self.END_CHARACTER

        prefix = word[0]
        suffix = word[1:]
        if prefix not in self.characters:
            self.characters[prefix] = Trie()

        self.characters[prefix].insert(suffix)

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if len(word) == 0:
            return self.END_CHARACTER in self.characters

        prefix = word[0]
        suffix = word[1:]
        if prefix not in self.characters:
            return False

        return self.characters[prefix].search(suffix)

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
