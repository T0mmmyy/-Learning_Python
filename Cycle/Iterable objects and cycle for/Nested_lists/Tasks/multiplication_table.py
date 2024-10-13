n, m = map(int, input().split())
a = []
count = 0
for i in range(1, n + 1):
    b = []
    for j in range(1, n + 1):
        b.append(i * j)
    a.append(b)
for x in range(n):
    for y in range(n):
        if a[x][y] == m:
            count += 1
print(count)