from typing import List
""" O(n * m) impl of alien dict. """

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj_l = {char: set() for w in words for char in w} # create O(n * m) adj_l

        for i in range(len(words) - 1): #O (n * m) with multiple constants
            w1, w2 = words[i], words[i + 1]
            minLen = min(len(w1), len(w2)) # min men word
            if (len(w1) > minLen and w1[:minLen] == w2[:minLen]):
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj_l[w1[j]].add(w2[j])
                    break
            
        
        visit, res = {}, []
        def dfs(c):
            if c in visit:
                return visit[c]
            
            visit[c] = True
            for child in adj_l[c]:
                if dfs(child):
                    return True

            visit[c] = False
            res.append(c)

        
        for c in adj_l:
            if dfs(c):
                return ""
        
        res.reverse()
        return "".join(res)

        

            


