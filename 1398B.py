t = int(input())
for _ in range(t):
    n = input()
    n = list(n)
    l=[]
    for i in range(len(n)):
        n[i] = int(n[i])
    for i in range(1,len(n)):
        if(n[i]==1):
            n[i]+=n[i-1]
    for i in range(len(n)-1):
        if n[i]!=0 and n[i+1]==0:
            l.append(n[i])
    if(n[-1]!=0):
        l.append(n[-1])
    l.sort(reverse=True)
    c=0
    for i in range(0,len(l),2):
        c+=l[i]
    print(c)
        