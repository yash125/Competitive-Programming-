a,b = map(int,input().split())
l1 = list(map(int,input().split()))
l1=l1[::-1]
m,n = map(int,input().split())

l2 = list(map(int,input().split()))
l2 = l2[::-1]

ans1=0
ans2=0

i=0
j=0

while(i<a):
    
    ans1+=(b**i)*l1[i]
    i+=1


while(j<m):
    
    ans2+=(n**j)*l2[j]
    j+=1

if(ans1==ans2):
    print("=")
elif ans1>ans2:
    print(">")
else:
    print("<")

    