n = int(input())
l=[]
for _ in range(n):
    a,b,c,d = map(int,input().split())
    l.append([a,b,c,d])
ans=[]
for i in range(len(l)):
    c=0
    for j in range(len(l)):
        if i==j:
            continue
        elif l[i][0]<l[j][0] and l[i][1]<l[j][1] and l[i][2]<l[j][2]:
            c=1
    if c==0:
        ans.append(l[i])
ans.sort(key = lambda x: x[3])
for i in range(len(l)):
    if l[i]==ans[0]:
        print(i+1)
        break



        
    
    