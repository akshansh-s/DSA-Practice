class Node:
    def __init__(self, val, k):
        self.right = None
        self.data = val
        self.left = None
        self.key = k

class Solution:
    # returns the inorder successor of the Node x in BST (rooted at 'root')
    def inorderSuccessor(self, root, x):
        if not root:
            return None
        if root.data>x.data:
            p=self.inorderSuccessor(root.left,x)
            if not p:
                return root
        else:
            p=self.inorderSuccessor(root.right,x)
        return p