from typing import List


class MinHeap:
    
    def __init__(self):
        self.heap = [0]

    def push(self, val: int) -> None:
        i = len(self.heap)
        self.heap.append(val)

        self._bubbleUp(i)


    def pop(self) -> int:
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()

        root = self.top()
        self.heap[1] = self.heap.pop()
        
        self._bubbleDown(1)
        return root
    
    def _bubbleUp(self, i):
        if i > 1:
            while i > 1 and self.heap[i // 2] > self.heap[i]:
                 self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]
                 i = i // 2


    def _bubbleDown(self, i):
        while ((i * 2) < len(self.heap)):
            if (i * 2 + 1 < len(self.heap) and
                self.heap[i * 2 + 1] < self.heap[i] and
                self.heap[i * 2 + 1] < self.heap[i * 2]):
                self.heap[i], self.heap[i * 2 + 1] = self.heap[i * 2 + 1], self.heap[i]
                i = i * 2 + 1

            elif (self.heap[i * 2] < self.heap[i]):
                self.heap[i], self.heap[i * 2] = self.heap[i * 2], self.heap[i]
                i = i * 2
            
            else:
                break


    def top(self) -> int:
        return self.heap[1] if len(self.heap) > 1 else -1

    def heapify(self, nums: List[int]) -> None:
        self.heap = [0] + nums

        for i in reversed(range(1, len(nums)//2 + 1)):
            self._bubbleDown(i)

        
        