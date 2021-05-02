n = int(input())
lst = [int(i) for i in input().split()][:n]
s= sum(lst)/4
import math
print(math.ceil(s))