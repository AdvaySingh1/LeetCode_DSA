# Definition for a pair.
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if len(pairs) <= 1:
            return pairs
        
        arr1 = self.mergeSort(pairs[:(len(pairs))//2])
        arr2 = self.mergeSort(pairs[(len(pairs))//2:])

        # using two pointers
        res = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if (arr1[i].key <= arr2[j].key):
                res.append(arr1[i])
                i += 1
                continue
            res.append(arr2[j])
            j += 1
        
        res.extend(arr1[i:])
        res.extend(arr2[j:])

        return res
    


    """
     - Time complexity: O(nlog(n)) because it is T = 2T(n/2) + n which is nlog(n)
     - Space complexity: O(n) as two arrays are made to store the data from the previous array
        The space complexity is really log(n) + n due to the size of the call stack and the arrays
        That's why it's dominated by the n and thus it is O(n).

    """



