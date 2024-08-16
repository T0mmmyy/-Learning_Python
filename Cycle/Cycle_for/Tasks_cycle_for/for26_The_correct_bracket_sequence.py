count = 0
n = list(input())
for i in n:
    if i == '(':
        count += 1
    else:
        count -= 1
        if count < 0:
            break
if count == 0:
    print('YES')
else:
    print('NO')