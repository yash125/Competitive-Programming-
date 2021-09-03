n = int(input())
left=[]
right=[]
for _ in range(n):
    
    a,b = map(int,input().split())
    if a<0:
        left.append([a,b])
    else:
        right.append([a,b])
left.sort(reverse=True)
right.sort()
i=0
j=0
ans=0
while(i<len(left) and j<len(right)):
    ans+=left[i][1]
    ans+=right[j][1]
    
    i+=1
    j+=1
if(i<len(left)):
    ans+=left[i][1]
if(j<len(right)):
    ans+=right[j][1]
print(ans)
    