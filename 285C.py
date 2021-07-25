n = int(input())
l = list(map(int,input().split()))
l.sort()
c=0
for i in range(len(l)):
    c+=abs(l[i]-(i+1))
print(c)