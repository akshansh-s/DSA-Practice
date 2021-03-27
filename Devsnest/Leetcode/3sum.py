res=[]
nums=[-1,0,1,2,-1,-4]
i=0
j=len(nums)-1
nums=sorted(nums)
while(i<=j):
    
    
    if (0-(nums[i]+nums[j])) in nums:
        k=nums.index(0-nums[i]-nums[j])
        
        if k!=i and k!=j and [nums[i],nums[k],nums[j]] not in res:
            res.append([nums[i],nums[k],nums[j]])
        
    if nums[i]+nums[j]>0:
        j-=1
    
    if nums[i]+nums[j]<0:
        i+=1
print(res)