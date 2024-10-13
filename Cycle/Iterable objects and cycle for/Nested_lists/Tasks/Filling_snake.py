n, m = map(int, input().split())
a = []
for i in range(n):
    a.append([0] * m)
count = 0
schet = 0
for i in range(n):
    if count == 0:
        for j in range(m):
            count = 1
            a[i][j] += schet
            schet += 1
    else:
        for x in range(1, m + 1):
            count = 0
            a[i][-x] += schet
            schet += 1
for y in range(n):
    print(*a[y])