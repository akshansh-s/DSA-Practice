class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[[]]
        nums.sort()
        for i in nums:
            ans+=[[i]+x for x in ans if [i]+x not in ans]
        return ans