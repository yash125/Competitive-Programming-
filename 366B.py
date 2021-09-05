n,k = map(int,input().split())
l = list(map(int,input().split()))

for i in range(len(l)):
    if (i-k)>=0:
        l[i]+=l[i-k]

h = 9999999999999
ind=-1
for i in range(len(l)-k,n):
    if l[i]<h:
        h = l[i]
        ind=i
print((ind%k)+1)