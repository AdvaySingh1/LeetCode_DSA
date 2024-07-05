from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

      # max heap (2 top values)
      """
      pop them from the heap. Add the resulting values depending on the vals.
      Return each value in the heap.
      While statement:
        heap lenght is greater than one
      """

      stones = [stone * -1 for stone in stones] # create a max heap
      heapq.heapify(stones)

      while len(stones) > 1:
        s1 = heapq.heappop(stones) * -1
        s2 = heapq.heappop(stones) * -1

        r = (abs(s1 - s2) * -1) 
        heapq.heappush(stones, r)
        
      return stones[0] * -1 if len(stones) > 0 else None