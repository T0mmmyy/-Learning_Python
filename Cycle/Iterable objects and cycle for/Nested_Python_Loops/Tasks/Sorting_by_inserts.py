n = int(input())
li = list(map(int, input().split()))
for i in range(1, n):
    for x in range(i, 0, -1):
        if li[x] < li[x - 1]:
            li[x], li[x - 1] = li[x - 1], li[x]
        else:
            break
print(*li)