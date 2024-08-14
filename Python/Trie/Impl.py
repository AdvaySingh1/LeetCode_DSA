""" All of the operations are done in O(m) time where m is the size of the string.
    This is beneficial over normal BSTs because it doesn't require log(n) time where n is the number of words in the database and can scale.
    It's beeficial over hashmaps which does things in a O(1) timescale because there's no way to look for prefixes with hashmaps
    
    It's commonly implemented is google search and other search algorithms. (Remember the contains function within ProveIt? That's
                                                                            a less efficient version with it's O(m*n logn)) time complexity."""


class TreeNode():
    def __init__(self):
        self.children = {}
        self.is_word = False

class PrefixTree:

    def __init__(self):
        self.root = TreeNode()

    def insert(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TreeNode()
            curr = curr.children[c]
        
        curr.is_word = True


    def search(self, word: str) -> bool:
        """Determines if a word is in the Dictionary

        Args:
            word (str): The Word To search

        Returns:
            bool: True if the word is in the Dictionary
        """
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return curr.is_word

    def startsWith(self, prefix: str) -> bool:
        curr = self.root

        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return True
        