n = int(input())
count = 0
l = list(map(int, input().split()))
for i in range(n):
    for x in range(n - 1 - i):
        if l[i] > l[i + 1]:
            count += 1
            l[i], l[i + 1] = l[i + 1], l[i]
print(*l)
print(count)