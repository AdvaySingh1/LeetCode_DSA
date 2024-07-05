class Node:
  def __init__(self, key: int, val: int):
    self.key, self.val = key, val
    self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
      # keep track of the usage
      self.capacity = capacity
      self.cache = dict()
      self.first, self.last = Node(0, 0), Node(0, 0)
      self.first.next, self.last.prev = self.last, self.first
      


    def get(self, key: int) -> int: # swap the last
      if key not in self.cache:
        return -1

        # remove it from the log
      self.cache[key].prev.next, self.cache[key].next.prev = self.cache[key].next, self.cache[key].prev
      self.cache[key].prev, self.cache[key].next = self.last.prev, self.last
      self.last.prev.next, self.last.prev = self.cache[key], self.cache[key]
      return self.cache[key].val
    

    def put(self, key: int, value: int) -> None:
      if (key in self.cache): 
        self.cache[key].val = value
        self.get(key)
        return
      elif (len(self.cache) == self.capacity):
        self.remove()
      self.insert(key, value)
      
    def insert(self, key: int, value: int) -> None:
      new_node = Node(key, value)
      self.cache[key] = new_node
      new_node.prev, new_node.next = self.last.prev, self.last
      self.last.prev.next = self.last.prev = new_node
    
    # len has to be greater than or equal to one.
    def remove(self) ->None:
      self.cache.pop(self.first.next.key)
      self.first.next.next.prev = self.first
      self.first.next = self.first.next.next

  