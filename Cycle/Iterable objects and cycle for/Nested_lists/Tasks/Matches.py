n = int(input())
schet = 0
a = []
count = 0
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
while schet < n:
    for i in range(n):
        if a[schet] == a[i]:
            continue
        else:
            if a[schet][0] == a[i][1]:
                count += 1
    schet += 1
print(count)