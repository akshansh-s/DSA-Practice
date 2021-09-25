import time
import math

def compute_pi(num_terms):
    total=0
    for x in range(num_terms):
        total=total+ ((-1)**x)/(2*x+1)
    return 4*total

print("Estimating Pi!\n")

request=7
print("========================================")
for exponent in range(request+1):
    start=time.time()
    result=compute_pi(10**exponent)
    stop=time.time()
    print("10^"+str(exponent)+"\t->",result,"\t",stop-start)
    print()
    
start=time.time()    
print("pi\t\t->",math.pi,"\t",time.time()-start)
print("="*40)
print("thank you, good bye!")