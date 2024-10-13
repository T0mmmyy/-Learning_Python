n, m = map(int, input().split())
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
for i in range(1, n):
    for x in range(1, m):
        a[i][x] += a[i - 1][x] + a[i][x - 1]
for l in range(n):
    print(*a[l], end=' ')
    print()