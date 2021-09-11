n = int(input())
l = list(map(int,input().split()))
d={}
c=0
ll = sorted(list(set(l)))
ans=False
for i in range(len(l)):
    if l[i] in d:
        d[l[i]].append(i+1)
    else:
        d[l[i]]=[i+1]
three=0
two=0
threeUtil = -1
for i in d:
    if len(d[i])>=3:
        three=1
        threeUtil= i
    elif len(d[i])>=2:
        two+=1
if(three==0 and two<=1):
    print("NO")
else:
    print("YES")
    ans=[]
    for i in ll:
        ans+=d[i]
    print(*ans)
    first=[]
    last=[]
    if three:
        for i in ll:
            if i<threeUtil:
                first+=d[i]
            elif i>threeUtil:
                last+=d[i]
        d[threeUtil][0],d[threeUtil][1] = d[threeUtil][1],d[threeUtil][0]
        print(*(first+d[threeUtil]+last))
        d[threeUtil][2],d[threeUtil][1] = d[threeUtil][1],d[threeUtil][2]
        print(*(first+d[threeUtil]+last))
    else:
        c=0
        for i in ll:
            ans=[]
            if c==2:
                break
            if len(d[i])>=2:
                d[i] = d[i][::-1]
                c+=1
                for j in ll:
                    ans+=d[j]
            print(*ans)
                    
            
            
        
            
            
        
    
                
                
    
    
    

        
    
    