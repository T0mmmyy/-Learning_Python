# n = int(input())
# a = []
# do = []
# posle = []
# for i in range(n):
#     b = list(map(int, input().split()))
#     a.append(b)
# for i in range(n):
#     for x in range(n):
#         if i == x:
#             break
#         do.append(a[i][x])
#     for j in range(x + 1, n):
#         posle.append(a[i][j])
# print(do, posle)
# if do == posle:
#     print('Yes')
# else:
#     print('No')
n = int(input())
a = []
flag = True
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)
for i in range(n):
    for x in range(n):
        if i == x:
            continue
        if a[i][x] != a[x][i]:
            flag = False
            break
    if not flag:
        break
if flag:
    print('Yes')
else:
    print('No')


