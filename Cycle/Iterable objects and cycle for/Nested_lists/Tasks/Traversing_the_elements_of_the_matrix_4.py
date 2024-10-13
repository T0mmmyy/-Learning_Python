a, b = map(int, input().split())
n = []
for i in range(a):
    li = list(map(int, input().split()))
    n.append(li)
for i in range(a-1, -1, -1):
    for x in range(b):
        print(n[i][x], end=' ')
    print()