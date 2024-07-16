
""" Overlapping dates. Note that although this implementation uses trees, the time complexity is O(n) worst case and O(log n) best case.
    Space complexity if O(n)."""

class Node:
    def __init__(self, L: int, R: int):
        self.L = L
        self.R = R
        self.left = None
        self.right = None


class MyCalendar:

    def __init__(self):
        self.root = None
        

    def book(self, start: int, end: int) -> bool:
        def _isValid(root, start, end) -> bool:
            if not root:
                return True
            if start >= root.R:
                return _isValid(root.right, start, end)
            elif end <= root.L:
                return _isValid(root.left, start, end)
            else:
                return False


        def _book(root, start, end) -> Node:
            if not root:
                return Node(start, end)
            if start >= root.R:
                root.right = _book(root.right, start, end)
            elif end <= root.L:
                root.left = _book(root.left, start, end)
            return root
        
        isValid = _isValid(self.root, start, end)
        if isValid:
            self.root = _book(self.root, start, end)
        return isValid
        

        

        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)