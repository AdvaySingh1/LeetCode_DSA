from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def bfs(root: TreeNode) -> None:
    queue = deque()

    queue.append(root)

    level = 1
    while (len(queue) > 0):
        print(level)
        curr = queue.popleft()
        for i in range(len(queue)):
            curr = queue.popleft()
            print (curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        level += 1
