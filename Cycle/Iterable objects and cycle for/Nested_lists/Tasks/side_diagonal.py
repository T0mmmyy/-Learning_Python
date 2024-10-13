n = int(input())
a = []
max_dioganal = 0
vrem = 0
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
for i in range(n):
        vrem = a[i][n - 1 - i]
        if vrem > max_dioganal:
            max_dioganal = vrem
print(max_dioganal)