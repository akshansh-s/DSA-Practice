'''Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.'''

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