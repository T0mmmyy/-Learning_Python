import math
okr = 0
ok = True
count = 0
n = int(input())
for i in range(n+1, n*2):
    sqrt = math.sqrt(i)
    okr = round(sqrt)
    for x in range(2, okr + 1):
        if i % x != 0:
            ok = True
        else:
            ok = False
            break
    if ok:
        count += 1
print(count)

def fsunction_name(i):
    print('finction code')

    return list





