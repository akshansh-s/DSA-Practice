class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        
        output=0
        max=-10000
        for start,end in sorted(intervals, key=lambda x: x[1]):
            if start>=max:
                max=end
            else:
                output+=1
        return output
        