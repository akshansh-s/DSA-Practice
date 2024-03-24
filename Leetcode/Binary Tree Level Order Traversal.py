class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []
        ans=[[]]
        q=[root,"X"]
        
        while True:
            n=q.pop(0)
            if n=="X":
                if len(q)==0:
                    return ans
                q.append("X")
                ans.append([])
            else:
                ans[-1].append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)