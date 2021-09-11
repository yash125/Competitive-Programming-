
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
s = set()
def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n + 1):
        if prime[p]:
            s.add(p)
SieveOfEratosthenes(999999)
n = int(input())
if(prime(n)):
    print(1)
    print(n)
elif prime(n-2):
    print(2)
    print(n-2,2)
elif n%2==0:
    for i in s:
        if n-i in s or prime(n-i):
            print(2)
            print(i,n-i)
            break
else:
    print(3)
    for i in s:
        if n-(2*i)>0 and ((2*i) in s or prime(n-(2*i))):
            print(i,i,n-2*i)
            break


