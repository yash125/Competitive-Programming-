import math
s = set()
def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):
        if (prime[p] == True):
 
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    for p in range(2, n+1):
        if prime[p]:
            s.add(p)

SieveOfEratosthenes(999999)
n = int(input())
l = list(map(int,input().split()))

for i in l:
    a = math.sqrt(i)
    if(a%1==0 and a in s):
        print("YES")
    else:
        print("NO")