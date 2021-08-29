n = int(input())
c = 0
h=n
while(h):
    c+=1
    h//=10
sub = 10**(c-1)-1
ans= (n-sub)*c
for i in range(1,c):
    ans+=(9*(10**(i-1)))*i
print(ans)

