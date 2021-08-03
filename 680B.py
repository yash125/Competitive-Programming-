n, m = map(int, input().split())
l = list(map(int, input().split()))
 
i = m - 1
j = m - 1
c = 0
while (i >= 0 and j < n):
    if (l[i] == 1 and l[j] == 1 and i == j):
        c += 1
    elif l[i] == 1 and l[j] == 1:
        c += 2
    i -= 1
    j += 1
 
while (i >= 0):
    c += l[i]
    i -= 1
while (j < n):
    c += l[j]
    j += 1
print(c)