'''Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.'''


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d={}
        ans=[]
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            
        while k>0:
            max_key = max(d, key=d.get)
            ans.append(max_key)
            del d[max_key]
            k-=1
        return ans


from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq,hp=Counter(nums),[]
        for element,count in freq.items():
            heapq.heappush(hp,(count,element))
            if len(hp)==k+1:
                heapq.heappop(hp)
        return [x[1] for x in hp]
