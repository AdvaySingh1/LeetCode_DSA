from typing import Optional

class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """ recursive approach """
        # def _helper(node, res):
        #     if node:
        #         res.append(node.val)
        #         _helper(node.left, res)
        #         _helper(node.right, res)

        #     return res
        # return _helper(root, [])

        stack = []
        res = []
        curr = root
        while curr or stack:
            if curr:
                stack.append(curr.right)
                res.append(curr.val)
                curr = curr.left
            else:
                curr = stack.pop()
        
        return res