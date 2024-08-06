n = int(input())
i = 0
s = 0
g = []
while i < n:
    ch = int(input())
    if ch <= 10:
        i += 1
        g.append(ch)
    else:
        s = ch % 10
        ch = ch // 10
        s = s + ch
        i += 1
        g.append(s)
print(*g, sep='\n')