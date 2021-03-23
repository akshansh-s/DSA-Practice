class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        d= len(matrix)
        r=len(matrix[0])
        spiral=[]
        l=0
        t=0
        while (t<d and l<r):
            for i in range(l,r):
                spiral.append(matrix[t][i])
            t+=1
            
            for i in range(t,d):
                spiral.append(matrix[i][r-1])
            r-=1
            
            if (t<d):   
                for i in reversed(range(l,r)):
                    spiral.append(matrix[d-1][i])
                d-=1
                
            if (l<r):
                for i in reversed(range(t,d)):
                    spiral.append(matrix[i][l])
                l+=1
        
        return spiral
    
    
    
    