n, m = map(int, input().split())
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
for i in range(n):
    sum_rows = 0
    for x in range(m):
        sum_rows += a[i][x]
    print(sum_rows, end=' ')
print()
for j in range(m):
    sum_column = 0
    for f in range(n):
        sum_column += a[f][j]
    print(sum_column, end=' ')