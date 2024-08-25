from typing import List


# O(n) implementation.

def shiftDown(nums: List[int], n: int, i: int) -> None:
    
    # start from the bottom most layer and replace all of the nodes if the children are smaller
    # * 2 + 1 and * 2 + 2


    smallest = i
    left, right = i * 2 + 1, i * 2 + 2

    if left < n and nums[left] < nums[smallest]:
        smallest = left
        

    if right < n and nums[right] < nums[smallest]:
        smallest = right
    
    if smallest != i:
        nums[i], nums[smallest] = nums[smallest], nums[i]
        shiftDown(nums, n, smallest)
    
def heapify(nums: List[int]):
    n = len(nums)
    for i in range(n // 2 - 1, -1, -1):
        shiftDown(nums, n, i)
    

def main():
    nums = [1, 6, 2, 34, 1, 9]
    heapify(nums)
    print(nums)

if __name__ == "__main__":
    main()



