def calculation(n):
    hm={}
    for i in input().split()[:n]:
        if i not in hm:
            hm[i]=1
        else:
            hm[i]+=1
            if hm[i]>n/2:
                return i
    return -1

n=int(input())
ans=calculation(n)
print(ans)