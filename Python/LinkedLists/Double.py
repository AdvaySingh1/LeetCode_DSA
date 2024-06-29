class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None # implicitly turns into another type
        self.prev = None # implicitly turns into another type because of dynamic language

# Implementation for Doubly Linked List
class LinkedList:
    def __init__(self):
        # set up dummy variables so we don't have to keep the size
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
 
    
    def insertFront(self, val):
        new_node = ListNode(val)
        new_node.prev = self.head # the one before the start
        new_node.next = self.head.next

        self.head.next.prev = new_node
        self.head.next = new_node # set it to the first node


    def insertEnd(self, val):
        new_node = ListNode(val)
        new_node.next = self.tail # the next is one past the end
        new_node.prev = self.tail.prev

        self.tail.prev.next = new_node
        self.tail.prev = new_node


    # Remove first node after dummy head (assume it exists)
    def removeFront(self):
        self.head.next = self.head.next.next
        if self.head.next:
            self.head.next.prev = self.head # no need to delete because of the decomposer

    # Remove last node before dummy tail (assume it exists)
    def removeEnd(self):
        self.tail.prev = self.node.prev.prev
        if self.tail.prev:
            self.tail.prev.next = self.tail


    def print(self):
        curr = self.head.next
        while curr.next:
            print(curr.val)
            curr = curr.next
