n = int(input())
l = list(map(int,input().split()))
d={}

for i in range(len(l)):
    if l[i]<=n and l[i] not in d:
        d[l[i]] = 1
    else:
        l[i] = -1

ind = 1


for i in range(len(l)):
    if l[i]==-1:
        
        while(ind<=n):
            if ind not in d:
                l[i] = ind
                d[ind]=1
                break
            else:
                ind+=1
print(*l)