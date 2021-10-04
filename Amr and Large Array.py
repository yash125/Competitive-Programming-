n = int(input())
l = list(map(int,input().split()))
d={}
for i in range(len(l)):
    if l[i] in d:
        d[l[i]][0]+=1
        d[l[i]][2] =i+1
    else:
        d[l[i]] = [1,i+1,i+1]
maxi = 0
diff = 99999999999999
l=-1
r=-1
for i in d:
    maxi = max(maxi,d[i][0])
for i in d:
    if d[i][0]==maxi:
        if diff>d[i][2]-d[i][1]:
            diff = d[i][2]-d[i][1]
            l = d[i][1]
            r = d[i][2]
print(l,r)
    