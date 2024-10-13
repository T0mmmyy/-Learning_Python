n, m = map(int, input().split())
a = []
maxx = 0
summ = 0
count = 0
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
for i in range(n):
    summ = 0
    for x in range(m):
        summ += a[i][x]
    if summ > maxx:
        maxx = summ
        count = i
print(maxx)
print(count)
