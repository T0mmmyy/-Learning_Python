a, b = map(int, input().split())
c, d = map(int, input().split())
count = 0
while c > 0 or d > 0:
    if c > 0 and d > 0:
        c, d = c - 1, d- 1
        count += b
    elif c > 0 and d == 0:
        c -= 1
        count += a
    else:
        d -= 1
        count += a
print(count)