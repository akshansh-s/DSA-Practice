class Tree:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def help (root,sm):
    if not root:
            return 0
    if root.right:
        if not root.right.left and not root.right.right:
            sm[0]+=root.right.val
    help(root.left,sm)
    help(root.right,sm)
    return sm[0]
        
class Solution:
    def solve(self, root):
        sm=[0]
        return help(root,sm)
        
        