import math


def prime(n):
    c=0
    sq = int(math.sqrt(n))
    for i in range(2,sq+1):
        if n%i==0:
            c=1
            break
    if c==0:
        return True
    return False

n = int(input())
ans=0
c=0
 
if prime(n):
    print(1)
elif n%2==0 or prime(n-2):
    print(2)
else:
    print(3)