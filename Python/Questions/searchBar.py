class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.is_word = True
        

    def search(self, word: str) -> bool:
        curr = self.root
        # use DFS with the tree structure

        # s = word.split()

        # need to use depth first search

        def _helper(curr: TrieNode, j) -> bool:
            for i in range(j, len(word)):
                if word[i] != ".":
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
                else:
                    for child in curr.children.values():
                        if _helper(child,  i + 1):
                            return True
                    return False
            
            return curr.is_word

        return _helper(curr, 0)
                        

            
        
        
                    

