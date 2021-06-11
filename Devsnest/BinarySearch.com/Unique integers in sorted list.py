class Solution:
    def solve(self, nums):
        n=0
        d={}
        for i in nums:
            if i not in d:
                d[i]=0
            d[i]+=1
        return len(d)