class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            mid = start + ((end - start) // 2) # to prevent overflow
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1 # needs to be the end because the operation floors it
            else:
                return mid
        
        return -1
            