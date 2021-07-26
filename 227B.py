n = int(input())
l = list(map(int,input().split()))
m = int(input())
h = list(map(int,input().split()))

d={}
for i in range(len(l)):
    d[l[i]]=i
ans1=0
ans2=0
for i in h:
    ans1+=d[i]+1
    ans2+=n-d[i]
print(ans1,ans2)
    
        