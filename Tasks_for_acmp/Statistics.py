n = int(input())
oc = list(map(int, input().split()))
chet = []
nechet = []
for i in range(len(oc)):
    if oc[i] % 2 == 0:
        chet.append(oc[i])
    else:
        nechet.append(oc[i])
if len(chet) >= len(nechet):
    print(*nechet)
    print(*chet)
    print('YES')
else:
    print(*nechet)
    print(*chet)
    print('NO')