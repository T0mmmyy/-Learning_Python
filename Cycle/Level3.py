n, k = map(int, input().split())
v = 240
ost = v - k
i = 1
vr = 0
while i <= n:
    if 5 * i <= ost:
        vr = vr + 1
        ost =  ost - 5 * i
    else:
        break
    i = i + 1
print(vr)