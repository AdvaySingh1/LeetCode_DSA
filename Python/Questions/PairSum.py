from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # O(1) space solution O(n) time

        fast, slow, prev = head, head, None
        while fast and fast.next:
            fast = fast.next.next
            tmp = slow
            slow = slow.next
            tmp.next = prev
            prev = tmp

        max_count = 0

        while slow:
            curr_count = prev.val + slow.val
            max_count = max(max_count, curr_count)
            slow, prev = slow.next, prev.next
        
        return max_count
            





        # determine the middle point.

        # add every one of the points into a string

        """ The following approach is O(n) time and space """
        # slow, fast = head, head
        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next
        
        # arr = []
        # while slow:
        #     arr.append(slow.val)
        #     slow = slow.next
        
        # max_sum = 0
        # for n in reversed(arr):
        #     curr_sum = head.val + n
        #     max_sum = max(max_sum, curr_sum)
        #     head = head.next
        
        # return max_sum
