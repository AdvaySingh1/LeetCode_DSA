
# chaining implementation
class Node:
    def __init__(self, key: int, val: int):
      self.key = key
      self.val = val
      self.next = None # make it a singaly linked list in the chance of a collision

class HashTable:
    
    def __init__(self, capacity: int):
      self.capacity = capacity
      self.table = [None] * self.capacity
      self.size = 0
    
    def _hash(self, key) -> int:
      return key % self.capacity # convers to ASCII implicitly

    def insert(self, key: int, value: int) -> None:
      i = self._hash(key)
      node = self.table[i]
      if not node:
          self.table[i] = Node(key, value)

      # if there's collision or the node exists
      else:
        prev = None
        while node:
          if node.key == key:
            node.val = value
            return
          prev, node = node, node.next # node no longet exists
        prev.next = Node(key, value) # prev is the last node in the chain

      self.size += 1
      if (self.size * 2 >= self.capacity):
            self.resize()



    def get(self, key: int) -> int:
      i = self._hash(key)
      node = self.table[i]
      while node:
        if node.key == key:
          return node.val
        node = node.next

      return -1 # usually add a position here
      # [] servers as an overloaded operatoer with a default None value
      # return [default] where it's a varibale and create a node with that key

    def remove(self, key: int) -> bool:
      i = self._hash(key)
      node = self.table[i]
      prev = None
      
      while node:
        if node.key == key:
          if prev:
            prev.next = node.next
          else:
            self.table[i] = node.next
          self.size -= 1
          return True
          
        prev, node = node, node.next

      return False




    def getSize(self) -> int:
      return self.size

    def getCapacity(self) -> int:
      return self.capacity
  
    def resize(self) -> None:
      self.capacity *= 2
      new_table = [None] * self.capacity

      for node in self.table:
        while node:
          i = self._hash(node.key)
          if not new_table[i]:
            new_table[i] = Node(node.key, node.val)
          else:
            new_node = new_table[i]
            while new_node.next:
              new_node = new_node.next
            new_node.next = Node(node.key, node.val)

          node = node.next
        
      self.table = new_table
      

