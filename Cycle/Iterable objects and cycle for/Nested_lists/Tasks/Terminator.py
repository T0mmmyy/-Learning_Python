n, m = map(int, input().split())
a = []
for i in range(n):
    data = input()
    a.append(list(data))
count = 0
sume = 0
for i in range(n):
    if 'S' not in a[i]:
        count += 1
        sume += m
for x in range(m):
    flag = True
    for j in range(n):
        if a[j][x] != 'S':
            continue
        else:
            flag = False
            break
    if flag:
        sume += n - count
print(sume)