
import heapq

""" The following is an implementation of two heaps for finding the min value in a stream of numbers.
    Brute force apprach: sort the seqeunce every time and return the median everytime.
     - This would be a O(n^2 log(n)) big omega approach if using mergesort and a O(n^3) big O approach if using quick sort.
    Our approach: using two different heaps. A small max heap and a large min heap."""

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:

        # push into appropriate heap
        if self.large and num > self.large[0]:
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, num * -1)
        # heapq.heappush(self.small, num * -1)
        # if (self.large and self.small[0] * -1 > self.large[0]):
        #     val = heapq.heappop(self.small)
        #     heapq.heappush(self.large, val * -1)
        
        # handle case where there's a size mismatch
        if (len(self.small) > len(self.large) + 1):
            val = heapq.heappop(self.small)
            heapq.heappush(self.large, val * -1)
        elif (len(self.small) + 1 < len(self.large)):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, val * -1)


    def findMedian(self) -> float:
        if (len(self.small) > len(self.large)):
            return self.small[0] * -1
        elif (len(self.small) < len(self.large)):
            return self.large[0]
        return ((self.small[0] * -1) + (self.large[0])) / 2
        