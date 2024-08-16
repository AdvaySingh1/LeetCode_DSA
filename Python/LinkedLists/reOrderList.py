from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """ou are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

Notice that in the general case for a list of length = n the nodes are reordered to be in the following order:

[0, n-1, 1, n-2, 2, n-3, ...]

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        # O(1) solution using slow and fast pointers
        # determine second half of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the slow pointer
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        
        # re order the list
        curr = head
        while prev.next:
            next_a, next_b = curr.next, prev.next
            curr.next = prev
            prev.next = next_a
            curr, prev = next_a, next_b



        # O(n) time and space approach
        # indexMap = {}

        # curr, i = head, 0
        # while curr:
        #     indexMap[i] = curr
        #     curr = curr.next
        #     i += 1

        # # now n is the length of the linked list
        # n = i

        # for i in range(math.ceil(n / 2)): # n = 2
        #     print(i, indexMap[i].val, indexMap[n - i - 1].val)
        #     indexMap[i].next = indexMap[n - i - 1]
        #     if i < math.ceil(n / 2) - 1:
        #         indexMap[n - i - 1].next = indexMap[i + 1]
        #     else:
        #         indexMap[n - i - 1].next = None
        




        # re ordering the linked list with dummy
        # while last:
        #     next = last.next
        #     prev = last
        #     prev.next = dummy.next
        #     dummy.next = prev
        #     last = next
        #     n += 1

        
        

        