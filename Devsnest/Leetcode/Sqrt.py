class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1 or x==0:
            return x
        
        l,r=0,x-1
        while l<=r:
            m=(l+r)//2
            if m*m==x:
                return m
            
            elif m*m>x:
                r=m-1
                
            elif m*m<x:
                ans=m
                l=m+1
                
        return ans
                
            