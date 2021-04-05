class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums=sorted(nums)
        for k in range(len(nums)-2):
            i=k+1
            j=len(nums)-1
            
            while (i<j):
                
                if nums[i]+nums[j]+nums[k]==0 and (nums[k],nums[i],nums[j]) not in res:
                    res.append((nums[k],nums[i],nums[j]))
                    i+=1
                    j-=1
                    continue
                elif nums[i]+nums[j]+nums[k]>0:
                    j-=1
                else:
                    i+=1
        
        return res