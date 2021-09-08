n, m = map(int, input().split())
a = min(n, m)
b = max(n, m)
c=0
while(a and b):
    if b>=a and b>=2 and a>=1:
        b-=2
        a-=1
        c+=1
    elif a>b and a>=2 and b>=1:
        a-=2
        b-=1
        c+=1
    else:
        break
print(c)