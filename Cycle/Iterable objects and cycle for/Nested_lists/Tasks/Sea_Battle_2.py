n, m = map(int, input().split())
a = []
# a = [input() for i in range(n)]
count = 0
for i in range(n):
    b = []
    f = str(input())
    for j in f:
        b.append(j)
    a.append(b)
for x in range(n):
    for y in range(m):
        if a[x][y] == '*' or a[max(0, x - 1)][y] == '*' or a[min(n - 1, x + 1)][y] == '*' or a[x][max(0, y - 1)] == '*' or a[x][min(m - 1, y + 1)] == '*':
            continue
        else:
            count += 1
print(count)