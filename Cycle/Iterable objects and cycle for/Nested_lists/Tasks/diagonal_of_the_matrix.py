n = int(input())
a = []
sum = 0
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
for i in range(n):
    for x in range(n):
        if i == x:
            sum += a[i][x]
print(sum)
