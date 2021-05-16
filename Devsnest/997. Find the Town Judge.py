class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        tc=[[0,0] for i in range(n+1)]
        for s,d in trust:
            tc[s][1]+=1
            tc[d][0]+=1
        for i in range(n+1):
            if tc[i][0]==n-1 and tc[i][1]==0:
                return i
        return -1
    