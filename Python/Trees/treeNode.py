class TreeNode:
    def __init__(self, val : int):
        self.val = val
        self.left = None
        self.right = None



"""
Insert into a BST Like this
"""

def insertIntoBST(self, root, val):
        if not root:
            return TreeNode(val)
        
        elif root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        
        else:
            root.left = self.insertIntoBST(root.left, val)
        
        return root


# delete a node from the BST
def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        elif (root.val < key):
            root.right = self.deleteNode(root.right, key)
        elif (root.val > key):
            root.left = self.deleteNode(root.left, key)
        else:
            if not root.right:
                return root.left
            elif not root.left:
                return root.right
            else:
                min_val = self.findMin(root.right)
                root.right = self.deleteNode(root.right, min_val)
                root.val = min_val
                
        return root
            
        
#find the min value of a BST
def findMin(self, root):
    if not root:
        return None
    while root and root.left:
        root = root.left
    return root.val

