a = []
flag = True
for i in range(4):
    n = str(input())
    b = []
    for j in n:
        b.append(j)
    a.append(b)

for x in range(3):
    for y in range(3):
        if a[x][y] == 'B':
            if a[x + 1][y] == 'B' and a[x][y + 1] == 'B' and a[x + 1][y + 1] == 'B':
                flag = False
                break
        elif a[x][y] == 'W':
            if a[x + 1][y] == 'W' and a[x][y + 1] == 'W' and a[x + 1][y + 1] == 'W':
                flag = False
                break
if flag:
    print('Yes')
else:
    print('No')