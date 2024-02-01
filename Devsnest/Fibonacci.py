'''Fibonacci Number
Math
Easy
Score: 10
Amazon
Microsoft
Adobe
JPMorgan
Infosys
Zillow
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.  
Given n, calculate F(n).

Try doing it in both recursive and iterative method

Input Format
First Parameter - Integer n

Output Format
Return the integer

Example 1:
Input:
    3
Output:
    2
Explanation:
    F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 2:
Input:
    4
Output:
    3
Explanation:
    F(4) = F(3) + F(2) = 2 + 1 = 3.
Constraints:
0 <= n <= 30'''

#recursion
def solve(n):
    if n<=1:
        return n
    else:
        return solve(n-1)+solve(n-2)

#Loops
def solve(n):
    # CODE HERE
    zero=0
    ans=0
    if n<=1:
        return n
    for i in range(2:n+1):
        a,b=b,a+b
    return b
    