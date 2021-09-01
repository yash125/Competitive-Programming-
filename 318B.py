n = input()
heavy=[0]*len(n)
metal = [0]*len(n)

for i in range(len(n)):
    
    if(i==0):
        if n[0:5]=="heavy":
            heavy[i]+=1
    else:
        if(n[i:i+5]=="heavy"):
            heavy[i]=heavy[i-1]+1
        else:
            heavy[i] = heavy[i-1]
for j in range(len(n)-2,-1,-1):
    if j+4<len(n):
        if(n[j:j+5]=="metal"):
            metal[j] = metal[j+1]+1
        else:
            metal[j] = metal[j+1]
c=0
ans=0
for i in range(len(n)):
    if c!=heavy[i]:
        ans+=metal[i]
        c = heavy[i]
print(ans)
    
    