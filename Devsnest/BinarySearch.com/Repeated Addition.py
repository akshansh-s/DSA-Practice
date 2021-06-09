class Solution:
    def solve(self, n):
        sum=0
        while n>0:    
            sum+=(n%10)
            n=n//10
            print(sum)
        if sum>=10:
            return self.solve(sum)
        return sum