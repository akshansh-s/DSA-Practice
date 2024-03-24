class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def gst(root,s):
    if not root:
        return s
    s=gst(root.right,s)
    root.val+=s
    s=root.val
    return gst(root.left,s)
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        gst(root,0)
        return root