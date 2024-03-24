class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        answer=[]
        a1=[]
        a2=[]
        x=len(nums)
        for i in range(x):
            a1.append(1)
            a2.append(1)
            answer.append(1)
            
        for i in range(x-1):
            a1[i+1]=a1[i]*nums[i]
            a2[x-2-i]=a2[x-i-1]*nums[x-i-1]
        
        for i in range(x):
            answer[i]=a1[i]*a2[i]
            
        return answer