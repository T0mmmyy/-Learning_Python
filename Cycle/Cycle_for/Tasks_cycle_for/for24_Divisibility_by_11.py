chet = 0
nechet = 0
n = list(map(int, input()))
for i in range(len(n)):
    if i % 2 == 0:
        chet += n[i]
    else:
        nechet += n[i]
if (nechet - chet) % 11 == 0:
    print('YES')
else:
    print('NO')