n = int(input())
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
for j in range(n):
    for x in range(n):
        print(a[x][j], end=' ')
    print()