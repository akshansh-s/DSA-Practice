class Solution:
    def isValid(self, s: str) -> bool:
        
        arr=[]
        par={"{":"}","(":")","[":"]"}
        
        for i in s:
            if i in par:
                arr.append(i)
            elif len(arr)!=0 and i==par[arr[-1]]:
                arr.pop()
            else:
                return False
        
        if len(arr)==0:
            return True
        else:
            return False