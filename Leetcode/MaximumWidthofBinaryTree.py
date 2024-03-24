class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
def getw(root,rootlevel,rootindex,wm):
    if root:
        if rootlevel not in wm:
            wm[rootlevel]=[rootindex,rootindex]
        elif rootindex<wm[rootlevel][0]:
            wm[rootlevel][0]=rootindex
        elif rootindex>wm[rootlevel][1]:
            wm[rootlevel][1]=rootindex
        getw(root.left,rootlevel+1,2*rootindex+1,wm)
        getw(root.right,rootlevel+1,2*rootindex+2,wm)

class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        widthmap={}
        getw(root,0,0,widthmap)
        return max(1+x[1]-x[0] for x in widthmap.values())