n = int(input())
l = list(map(int,input().split()))
c = 0
i = 0
ans=0
while(c<n):
    
    if(i==0 and c<n):
        ans+=1
        while(i<n):
            if(c>=l[i]):
                c+=1
                l[i]=1002
                # print(i,c,ans)
            i+=1
        if(i==n):
            i-=1
        
    if(i==n-1 and c<n):
        ans+=1
        while(i>=0):
            if(c>=l[i]):
                c+=1
                l[i]=1002
                # print(i,c,ans)
            i-=1
        if(i==-1):
            i+=1
            
    
print(ans-1)
            
        
            
            
