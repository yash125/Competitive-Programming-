n = int(input())
m = input()
left = [0]*n
right = [0]*n
left_flag=False
right_flag = False
for i in range(n):
    if left_flag:
        left[i] = left[i-1]+1
    if(m[i]=='R'):
        left_flag = True
        left[i] = 1 
    elif m[i]=='L':
        left_flag = False
for i in range(n-1,-1,-1):
    if right_flag:
        right[i] = right[i+1]+1
    if(m[i]=='L'):
        right_flag = True
        right[i] = 1
    elif m[i]=='R':
        right_flag = False

c=0
for i in range(n):
    if(left[i]==right[i]):
        c+=1
print(c)