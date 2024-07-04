""" Implementation one. Using quickselect. T = T(n/2) + n in the best case which has an average case of n"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        start, end = 0, len(nums) - 1
        k = len(nums) - k

        while (start < end):
            pivot = self.partition(nums, start, end)

            if pivot < k:
                start = pivot + 1
            
            elif pivot > k:
                end = pivot - 1
            
            else:
                break

        return nums[k]
        # Quick Select

    
    def partition(self, nums: List[int], start, end):
        pivot, j = nums[end], start

        for i in range(start, end):
            if nums[i] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                j+=1
            
        nums[j], nums[end] = nums[end], nums[j]

        return j
    



""" 
Implmentation two. Using the heap. Heap creation T = n. Heapify T = n. Heapify = O(log(n)). Then inserting each element is also O(log(n)).
Therefore, the total time complexity is O(n).
This does, however, have a space complexity of O(n) since it's creating the heap array.
"""
import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = nums[0:k] # O(n) is a dynamic array
        heapq.heapify(heap) # O(n^2)

        # current length if k since that's how many elements are bigger
        for num in nums[k:]:
            heapq.heappushpop(heap, num)
        
        return heap[0]