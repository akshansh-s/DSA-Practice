'''A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l,r=0,len(s)-1
        s=s.lower()
        
        while l<=r:
            if s[l]==s[r]:
                l+=1
                r-=1
                continue
            elif (s[l]<'a' or s[l]>'z') and (s[l]<'0' or s[l]>'9'):
                l+=1
            elif (s[r]<'a' or s[r]>'z') and (s[r]<'0' or s[r]>'9'):
                r-=1
            
            else:
                return False
        return True