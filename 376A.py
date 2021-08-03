n = input()
c = n.find('^')
left = 0
right = 0
for i in range(len(n)):
    if n[i]!='=' and n[i]!='^':
        if(i<c):
            left+=int(n[i])*(c-i)
        else:
            right+=int(n[i])*(i-c)
if(left>right):
    print("left")
elif right>left:
    print("right")
else:
    print("balance")
        
    
    