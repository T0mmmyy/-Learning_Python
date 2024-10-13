t = int(input())

#n - Кол-во интервалов
#s - время для принятия душа
#m - кол во минут в сутках

sc = 0
yesno = []
while sc < t:
    ok = False
    interval = []
    max_interval = 0
    n, s, m = map(int, input().split())
    for i in range(n):
        a, b = map(int, input().split())
        interval.append(a)
        interval.append(b)
    if interval[0] >= s or m - interval[-1] >= s:
        ok = True
    else:
        for x in range(1, len(interval) - 1, 2):
            count = 0
            for j in range(interval[x], interval[x + 1]):
                count += 1
                if count > max_interval:
                    max_interval = count
        if max_interval >= s:
            ok = True
    if ok:
        yesno.append('YES')
    else:
        yesno.append('NO')
    sc += 1
print(*yesno, sep='\n')