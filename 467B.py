n,m,k = map(int,input().split())
l = []
for _ in range(m):
    a = bin(int(input())).replace("0b", "")
    a=a[::-1]
    l.append(a)
fr =bin(int(input())).replace("0b", "")
h = fr.count('1')
fr = fr[::-1]
ans=0
for kk in range(len(l)):
    i=0
    j=0
    c=0
    while(i<len(fr) and j<len(l[kk])):
        if (fr[i]=='1' or l[kk][j]=='1') and l[kk][j]!=fr[i]:
            c+=1
        i+=1
        j+=1
    while(i<len(fr)):
        if fr[i]=='1':
            c+=1
        i+=1
    while(j<len(l[kk])):
        if l[kk][j]=='1':
            c+=1
        j+=1
    if(c<=k):
        ans+=1
print(ans)
            


