n = int(input())
l = list(map(int,input().split()))
d={}
for i in range(len(l)):
    if l[i] in d:
        
        d[l[i]].append(i)
    elif l[i] not in d:
        d[l[i]]=[i]
l=[]
for i in d:
    if len(d[i])==1:
        l.append([i,0])
    else:
        h=0
        a = d[i][1]-d[i][0]
        for j in range(1,len(d[i])):
            if(d[i][j]-d[i][j-1]!=a):
                h=1
                break
        if(h==0):
            l.append([i,d[i][1]-d[i][0]])
        
l.sort()
print(len(l))
for i in l:
    print(*i)