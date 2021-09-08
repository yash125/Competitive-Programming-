import sys
input = sys.stdin.readline
n = int(input())
l=[]
d={}
for _ in range(n):
    a,b = map(int,input().split())
    l.append([a,b])
    if a in d:
        d[a]+=1
    else:
        d[a]=1
for i in range(len(l)):
    left = n-1
    if l[i][1] in d:
        left+=d[l[i][1]]
        right = (n-1)-d[l[i][1]]
    else:
        right = n-1
    print(left,right)
        
        