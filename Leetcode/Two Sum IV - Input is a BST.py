class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def dll(root):
    if not root:
        return None, None
    lh,lt=dll(root.left)
    rh,rt=dll(root.right)
    if lh:
        h=lh
        lt.right=root
        root.left=lt
    else:
        h=root
    if rh:
        t=rt
        rh.left=root
        root.right=rh
    else:
        t=root
    return h,t
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        h,t=dll(root)
        while h.val!=t.val:
            sum=h.val+t.val
            if sum==k:
                return True
            if sum<k:
                h=h.right
            else:
                t=t.left
        return False

'''class Solution:
    def inorder(self,root,a):
        if root:
            self.inorder(root.left,a)
            a.append(root.val)
            self.inorder(root.right,a)
        
    def findTarget(self, root: TreeNode, target: int) -> bool:
        nums=[]
        self.inorder(root,nums)
        l=0
        r=len(nums)-1
        while l<r:
            if nums[l]+nums[r]<target:
                l+=1
            elif nums[l]+nums[r]>target:
                r-=1
            elif nums[l]+nums[r]==target:
                return True
        return False'''