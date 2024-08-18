
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        list_map = {None: None} # Nodes previous, curr

        curr = head
        while curr:
            new_curr = Node(curr.val)
            list_map[curr] = new_curr
            curr = curr.next
        
        curr = head

        while curr:
            list_map[curr].next = list_map[curr.next]
            list_map[curr].random = list_map[curr.random]
            curr = curr.next

        return list_map[head]

        list_map = {} # Nodes previous, curr

        curr = head
        while curr:
            new_curr = Node(curr.val)
            list_map[curr] = new_curr
            curr = curr.next
        
        curr = head

        while curr:
            list_map[curr].next = list_map[curr.next] if curr.next else None
            list_map[curr].random = list_map[curr.random] if curr.random else None
            curr = curr.next

        return list_map[head] if head in list_map else None
        

            

        
                

