"""
Build a tree based on inorder and preorder treversal O(n) time and space
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder or len(preorder) != len(inorder):
            return None
        
        if len(preorder) == 0:
            return None
        
        m = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:m+1], inorder[:m])
        root.right = self.buildTree(preorder[m+1:], inorder[m+1:])

        return root


        