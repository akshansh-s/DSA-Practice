n=int(input())

for i in range(n):
    print("")
    for j in range(n-i):
        print("-",end="")

    for j in range(i+1):
        print(n-j,end="-")

for i in reversed(range(n)):
    print("")
    for j in range(n-i):
        print("-",end="")

    for j in range(i+1):
        print(n-j,end="-")