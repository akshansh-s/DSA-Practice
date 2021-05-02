n=int(input())
lst = [int(i) for i in input().split()][:n]
h,v=0,0
for i in range(1,n-1):
    if lst[i]>lst[i+1] and lst[i]>lst[i-1]:
        h+=1
    elif lst[i]<lst[i+1] and lst[i]<lst[i-1]:
        v+=1
print(h,v)
    