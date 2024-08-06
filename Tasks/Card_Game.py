col = int(input())
sunit = 0
s = 0
i = 0
play = 0
while i < col:
    a1, a2, b1, b2 = map(int, input().split())
    while play < 4:
        if a1 > b1:
            s += 1
        elif a2 > b2:
            s += 1
        else:
            s += 0
        if