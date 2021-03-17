class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        numap=set()
        for num in nums:
            if num not in numap:
                numap.add(num)
            else:
                return True
                
        return False