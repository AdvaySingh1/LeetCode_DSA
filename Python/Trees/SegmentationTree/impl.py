from typing import List


"""
 * The following is an implementation of segmentation trees.
 * These are useful for range based queries with updates.
 * Worst case range-based queries are O(n). This method allows O(1) updates.
 * The prefix-suffix implmentation allows for an O(1) determination of ranges, but requires O(n) to create and doesn't allow updates (they would also be O(n)).
 * This method of the segment trees allows for an O(n) time for creating but allows updates and range based queries in O(log n) time.
 * Why O(log n) for querying? Refer to https://vscode.dev/github/AdvaySingh1/LeetCode_DSA/blob/main/c%2B%2B/Trees/SegmentationTrees/impl.cpp#L88 (line 88).
 * Here since each node has a value rather than just the sum, the max number of nodes accessed at any height in the tree is 4, hence, O(log n).
 * This can also be implemented with arrays. However, the last two  levels are not always complete like heaps and therefore this implementation is preferred.
 """

class Node:
    def __init__(self, val, L: int, R: int):
        self.sum = val
        self.L = L
        self.R = R
        self.left = None
        self.right = None
        

class SegmentTree:
    
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)

    def build(self, nums, L: int, R: int) -> Node:
        if (L == R):
            return Node(nums[L], L, R)
        
        m = (R + L) // 2
        root = Node(0, L, R)
        root.left = self.build(nums, L, m)
        root.right = self.build(nums, m + 1, R)

        root.sum = root.left.sum + root.right.sum
        return root


    
    def update(self, index: int, val: int) -> None:
        def _update(root: Node, index: int, val: int) -> None:
            if root.L == root.R:
                root.sum = val
                return
            
            m = (root.R + root.L) // 2
            if (m >= index):
                _update(root.left, index, val)
            else:
                _update(root.right, index, val)
            root.sum = root.left.sum + root.right.sum

        _update(self.root, index, val)


    
    def query(self, L: int, R: int) -> int:

        def _query(root: Node, L: int, R: int) -> int:
            if (root.R == R and root.L == L) or (root.R == root.L):
                return root.sum
            
            m = (root.R + root.L) // 2

            if (L > m):
                return _query(root.right, L, R)
            elif (R <= m):
                return _query(root.left, L, R)
            else:
                return _query(root.left, L, m) + _query(root.right, m + 1, R)
            
        return _query(self.root, L, R)