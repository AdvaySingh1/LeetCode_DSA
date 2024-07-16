from typing import Optional

# two stacks


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        visited, stack, res = [], [], []
        curr = root
        visited.append(0)
        stack.append(curr)

        while stack:
            curr = stack.pop()
            v = visited.pop()
            if curr:
                if v:
                    res.append(curr.val)
                else:
                    stack.append(curr)
                    visited.append(1)
                    stack.append(curr.right)
                    visited.append(0)
                    stack.append(curr.left)
                    visited.append(0)
        
        return res