# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []

        for i in range(len(pairs)):
            p = i
            while p > 0 and pairs[p - 1].key > pairs[p].key: # won't run the first time
                temp = pairs[p]
                pairs[p] = pairs[p-1]
                pairs[p-1] = temp
                p -= 1
            res.append(pairs[:]) # make a copy or else each item in the list will point to the same
            # such as res = [[0] * 4] * 4 where all of the rows will be the same pointer
        
        return res
    

  """
  This is a stable sorting algorithms since the values stay in order
  This is beg theta n and O(n^2)
  """