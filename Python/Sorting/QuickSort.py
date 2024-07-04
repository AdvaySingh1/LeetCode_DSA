"""Non-stable sorting algorithms. O(logn) space complexity and O(nlogn) best case and O(n^2) worst case time complexity."""
class Solution:

    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs:
            return None
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

    def quickSortHelper(self, pairs: List[Pair], start, end):
        if end - start >= 1:
            pivot = pairs[end]

            left = start

            for i in range(start, end):
                if pairs[i].key <= pivot.key:
                    temp = pairs[i]
                    pairs[i] = pairs[left]
                    pairs[left] = temp
                    left += 1

            pairs[end] = pairs[left]
            pairs[left] = pivot

            self.quickSortHelper(pairs, start, left - 1)
            self.quickSortHelper(pairs, left + 1, end)



"""The following implementation has O(n) space complexity because of arr[:] slicing the array and creating a copy
    rather than the origional pointer. However, this implementation tends to be stable.
"""
# class Solution:
#     def quickSort(self, pairs: List[Pair]) -> List[Pair]:
#         if not pairs or len(pairs) == 0:
#             return [] # can't merge none type so merge an empty array
        
#         if len(pairs) <= 1:
#             return pairs

#         pivot = pairs[-1]

#         left = 0


#         for i in range(len(pairs) - 1):
#             if pairs[i].key < pivot.key:
#                 temp = pairs[i]
#                 pairs[i] = pairs[left]
#                 pairs[left] = temp
#                 left += 1
        
#         pairs[-1] = pairs[left]
#         pairs[left] = pivot


#         return (self.quickSort(pairs[:left]) + 
#         [pivot] + (self.quickSort(pairs[left+1:])))
    

    """
    Time complexity: is O(n log n) in the best (and average case if implemented right) and O(n^2) otherwise
    Space commplexity: this is better than merge sort: O(log(n)) since that's the number of stacks. This can also be O(n)
        How to optimize: choosing the right pivot. Choose a pivot which is guranteed to have values of all sizes for example,
        take the first and last values and make that the pivot.
        - Can potentially choose the nth largest element and then choose the pivot.
    """