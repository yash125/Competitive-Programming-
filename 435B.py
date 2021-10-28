n,k = input().split()
k = int(k)
n = list(n)
for i in range(len(n)):
    n[i] = int(n[i])
for i in range(len(n)):
    x=n[i]
    y=i
    for j in range(i+1,len(n)):
        if(n[j]>x and (j-i)<=k):
            x = n[j]
            y = j
    k-=(y-i)
    if(x!=n[i]):
        for h in range(y,i,-1):
            n[h] = n[h-1]
    n[i] = x
ans=""
for i in n:
    ans+=str(i)
print(ans)
        
    
            
        