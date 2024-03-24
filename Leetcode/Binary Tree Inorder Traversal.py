class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        l=[]
        def ino(root,l):
            if root:
                ino(root.left,l)
                l.append(root.val)
                ino(root.right,l)
            return l
        return ino(root,l)