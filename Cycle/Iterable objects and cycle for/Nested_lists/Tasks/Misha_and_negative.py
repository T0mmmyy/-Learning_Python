n, m = map(int, input().split())
count = 0
a = []
for i in range(n):
    b = []
    d = str(input())
    for j in d:
        b.append(j)
    a.append(b)
input()
g = []
for x in range(n):
    b = []
    d = str(input())
    for y in d:
        b.append(y)
    g.append(b)

for v in range(n):
    for s in range(m):
        if a[v][s] == 'W' and g[v][s] == 'B' or a[v][s] == 'B' and g[v][s] == 'W':
            continue
        else:
            count += 1
print(count)