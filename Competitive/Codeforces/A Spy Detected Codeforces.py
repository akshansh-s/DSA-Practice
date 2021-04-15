'''t=int(input())
for i in range(t):
    n=int(input())
    for j in range(n):
        arr=[]
        x=list(map(int, input().strip().split(' ')))
        arr.append(x)

for j in arr:
    for i in range(len(j)-2):
        if j[i]!=j[i+1]:
            ans= i if j[i+1]==j[i+2] else i+1
            print(ans)
        else:
            continue'''

from collections import Counter
b=int(input())
for s in range(b):
    z=int(input())
    a=input().split(' ')
    c=Counter(a)
    for i in c:
        if c[i]==1:
            print((a.index(i))+1)
            break
