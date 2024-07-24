from typing import Optional

"""
 * The following impl is also the same time and space complexity as the recursive iteration (O(n) space and O(n) time (prove using divide and conquer strong induction)).
 * Difference from the normal recursive implementation: we have our own cute lil stack.
 *
 * Space is theta(log n) and O(n) no omega.
 * What to prove: T(n) = T(k) + T(n-k-1) + O(1) = O(n) (omega in this case).
 """


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.res = []

        stack = []
        # add the values appropriatly
        curr = self.root
        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                self.res.append(curr.val)
                curr = curr.right

    def next(self) -> int:
        return self.res.pop(0)

    def hasNext(self) -> bool:
        if self.res:
            return True
        return False