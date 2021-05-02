t=int(input())
for _ in range(t):
    
    b,h = list(map(float, input().split()))
    ans=0.0
    if h%2==0:
        h=h/2
    else:
        b=b/2
    while h>0:
        ans+=b
        h-=1
    formatted_float = "{:.2f}".format(ans)
    print(formatted_float)