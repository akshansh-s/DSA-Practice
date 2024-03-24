'''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s)!=len(t):
            return False
        sm={}
        
        for c in s:
            if c not in sm:
                sm[c]=1
            else:
                sm[c]+=1
        
        for c in t:
            if c not in sm:
                return False
            else:
                sm[c]-=1
                if sm[c]==0:
                    del sm[c]
        
        if len(sm)!=0:
            return False
        
        return True
        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=sorted(s)
        t1=sorted(t)
        return s1==t1
            