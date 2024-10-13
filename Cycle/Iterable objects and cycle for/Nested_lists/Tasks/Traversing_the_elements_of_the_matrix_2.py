n = int(input())
a = []
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
for i in range(n-1, -1, -1):
    for x in range(n-1, -1, -1):
        print(a[x][i], end=' ')
    print()