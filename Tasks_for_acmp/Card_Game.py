n = int(input())
sunit = 0
i = 0
g = []
def card(): #  3 8 2 6 пример
    count = 0
    a, a1, b, b1 = map(int, input().split())
    if a > b:
        if a1 > b1:
            count += 1
    if a > b1:
        if a1 > b:
            count += 1
    if a1 > b1:
        if a > b:
            count += 1
    if a1 > b:
        if a > b1:
            count += 1
    g.append(count)
while i < n:
    card()
    i += 1
print(*g, sep='\n')