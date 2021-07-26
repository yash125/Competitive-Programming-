t = int(input())
l=[]
for _ in range(t):
    a,b = map(int,input().split())
    l.append([a,b])
c=0
for i in range(len(l)):
    left=0
    right=0
    upper=0
    lower=0
    for j in range(len(l)):
        if l[i][0]==l[j][0] and l[i][1]==l[j][1]:
            continue
        elif l[i][0]>l[j][0] and l[i][1]==l[j][1]:
            left+=1
        elif l[i][0]<l[j][0] and l[i][1]==l[j][1]:
            right+=1
        elif l[i][0]==l[j][0] and l[i][1]>l[j][1]:
            lower+=1
        elif l[i][0]==l[j][0] and l[i][1]<l[j][1]:
            upper+=1
    if upper>0 and lower>0 and left>0 and right>0:
        c+=1
print(c)