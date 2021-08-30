n,m,k = map(int,input().split())
a = list(map(int,input().split()))

a.sort(reverse=True)
ans=0
i=0
c=0
while(i<n and c<m):
    if k>=(m-c):
        c+=m-c
        break
    if k<=0:
        c+=(a[i]-1)
    else:
        c+=a[i]
    
    i+=1
    ans+=1
    k-=1
if(c>=m):
    print(ans)
else:
    print(-1)
    