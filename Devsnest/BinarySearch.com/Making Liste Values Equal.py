class Solution:
    def solve(self, nums):
        nums=sorted(nums)
        return nums[-1]-nums[0]