
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        counts = Counter(nums)

        j = 0
        for i in range(3):
            for p in range(counts[i]):
                nums[j] = i
                j += 1


        return nums
    

    """Note this implementation is still only O(n) although there's nested loop because j will only be the size of the array."""
        