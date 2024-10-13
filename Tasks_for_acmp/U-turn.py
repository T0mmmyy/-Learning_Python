n = int(input())
a = list(map(int, input().split()))
for j in range(n):
    print(a.pop(), end=' ')