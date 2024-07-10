n, m = map(int, input().split())
h = list(map(int, input().split()))
g = list(map(int, input().split()))
result = []
j = h + g
i = 0
while len(j) > 0:
    i = min(j)
    result.append(i)
    j.remove(i)
print(*result)