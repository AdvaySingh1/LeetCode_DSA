from typing import List

""" These fon't have duplicates """

"""The tome complexity of the following solution is k 2 ^ n """

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        subset, res = [], []
        
        def combineHelper(n, k, i):
            if len(subset) == k:
                res.append(subset[:])
                return
            
            if i <= n:
                subset.append(i)
                combineHelper(n, k, i + 1)
                subset.pop()
                combineHelper(n, k, i + 1)
            
        combineHelper(n, k, 1)

        return res
    


    """ The following is the bonimial apprach for n choose k """


    """ These fon't have duplicates """

"""The tome complexity of the following solution is k 2 ^ n """

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        subset, res = [], []
        
        def combineHelper(n, k, i):
            if len(subset) == k:
                res.append(subset[:])
                return
            
            for j in range(i, n + 1):
                subset.append(j)
                combineHelper(n, k, j + 1)
                subset.pop()

        combineHelper(n, k, 1)
        return res

            


            
