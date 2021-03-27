class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res=[]
        test=False
        for i in nums1:
            n=nums2.index(i)
            for j in range(n,len(nums2)):
                if nums2[j]>i:
                    res.append(nums2[j])
                    test=True
                    break
            if test==False:
                res.append(-1)
            test=False
            
        return res