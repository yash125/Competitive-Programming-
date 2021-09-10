n,a,b,c,d = map(int,input().split())
 
ans = max(abs((a+b)-(d+c)),abs((d+b)-(a+c)))
c = n-ans
c*=n
print(max(0,c))