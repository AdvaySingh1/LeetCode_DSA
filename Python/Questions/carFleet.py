from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pairs = [[position[i], speed[i]] for i in range(len(position))]
        pairs.sort(key=lambda pair: pair[0], reverse=True)

        stack = []
        for pair in pairs:
            time = (target - pair[0]) / pair[1]
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)

        


