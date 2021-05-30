class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        ans=[]
        tc=[[0,0] for i in range(n)]
        for s,d in edges:
            tc[s][1]+=1
            tc[d][0]+=1
        for i in range(n):
            if tc[i][0]==0:
                ans.append(i)
        return ans