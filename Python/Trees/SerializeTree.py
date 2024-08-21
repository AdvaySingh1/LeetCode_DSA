

from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right





""" Doing so with pre order and in order traversal. """
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s = []
        # pre order string
        def helper(root) -> None:
            if root:
                s.append(str(root.val))
                helper(root.left)
                helper(root.right)

        # in order string
        def helper2(root) -> None:
            if root:
                helper2(root.left)
                s.append(str(root.val))
                helper2(root.right)

        helper(root)
        s.append("#")
        helper2(root)

        res = ",".join(s)
        return res




        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return
        pos, ios = data.split("#")
        pos, ios = pos.split(",")[:-1], ios.split(",")[1:]
 

        def helper(pos, ios):
            if not pos or not ios or len(pos) != len(ios):
                return None

            m, root = ios.index(pos[0]), TreeNode(pos[0])

            root.left = helper(pos[1:m+1], ios[0:m])
            root.right = helper(pos[m+1:], ios[m+1:])
            return root
        return helper(pos, ios)




""" Doing so with only in order treversal"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # O(n) time where n is the number of nodes in the tree
    # O(h) space where h is the height of the tree (due to call stack)
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s = []
        # pre order string
        def helper(root) -> None:
            if root:
                s.append(str(root.val))
                helper(root.left)
                helper(root.right)
            else:
                s.append("n")

        helper(root)
        res = ",".join(s)
        return res




        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data, self.i = data.split(","), 0
        print(data)

        def helper() -> TreeNode:
            if self.i >= len(data):
                return

            if data[self.i] == "n":
                self.i += 1
                return
            
            root = TreeNode(data[self.i])
            self.i += 1
            root.left = helper()
            root.right = helper()
            return root

        return helper()






""" Breath first search"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # O(n) time where n is the number of nodes in the tree
    # O(h) space where h is the height of the tree (due to call stack)
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        s = []

        def bfs(root):
            queue, res = deque(), []
            queue.append(root)
            while queue:
                for i in range(len(queue)):
                    node = queue.popleft()

                    if not node:
                        res.append("n")
                    else:
                        res.append(str(node.val))
                        queue.append(node.left)
                        queue.append(node.right)
                res.append("l")
            return res

        return (",".join(bfs(root)))
    
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = [[item for item in level.split(",") if item] for level in data.split("l") if level]
        indecies = {l: 0 for l in range(len(data))}


        def build(l):
            if data[l][indecies[l]] == "n":
                indecies[l] += 1
                return None
            
            node = TreeNode(data[l][indecies[l]])
            indecies[l] += 1
            node.left = build(l + 1)
            node.right = build(l + 1)

            return node

        
        return build(0)




                


 



