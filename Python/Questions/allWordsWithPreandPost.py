from typing import List

""" Determining how many words there are in the list with a given pre and a post fix """

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class WordFilter:

    def __init__(self, words: List[str]):
        self.words = words


        
        """ init a pre and a post treeNode """

        #pre
        self.preRoot, self.postRoot = TrieNode(), TrieNode()
        
        for i in range(len(words)):
            pre_curr, post_curr = self.preRoot, self.postRoot
            for j in range(len(words[i])):
                pre_c, post_c = words[i][j], words[i][-j - 1]
                if pre_c not in pre_curr.children:
                    pre_curr.children[pre_c] = TrieNode()
                if post_c not in post_curr.children:
                    post_curr.children[post_c] = TrieNode()
                pre_curr, post_curr = pre_curr.children[pre_c], post_curr.children[post_c]
            
            pre_curr.is_word = True
            post_curr.is_word = True



    def f(self, pref: str, suff: str) -> int:
        pref_set = set()

        # make sure they have the roots (with a pointer to the end)
        pre, post = self.preRoot, self.postRoot
        for c in pref:
            if c not in pre.children:
                return 0
            pre = pre.children[c]
        for c in suff:
            if c not in post.children:
                return 0
            post = post.children[c]


        def pref_dfs(curr, word: list):
            if curr.is_word:
                pref_set.add("".join(word))
            
            for child in curr.children:
                word.append(child)
                pref_dfs(curr.children[child], word)
                word.pop()

        
        def post_dfs(curr, word: list, res: int):
            if curr.is_word:
                if ("".join(word))[::-1] in pref_set:
                    print(word)
                    res += 1

            for child in curr.children:
                word.append(child)
                res += post_dfs(curr.children[child], word, res)
                word.pop()
            
            return res
            


        
        pref_dfs(pre, pref.split())
        return post_dfs(post, suff.split(), 0)



# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)