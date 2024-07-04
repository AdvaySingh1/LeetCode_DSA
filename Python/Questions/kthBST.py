





# another possible implementation
# class Solution:
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         count = 1 + self.nodeCounter(root.left)

#         if count < k:
#             return self.kthSmallest(root.right, k - count)
        
#         elif count > k:
#             return self.kthSmallest(root.left, k)
        
#         else:
#             return root.val
    


#     def nodeCounter(self, root):
#         if not root:
#             return 0
#         else:
#             return (1 + self.nodeCounter (root.left) 
#                     + self.nodeCounter(root.right))