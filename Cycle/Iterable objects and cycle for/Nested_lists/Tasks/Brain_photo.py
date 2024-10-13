n, m = map(int, input().split())
a = []
ok = True
for i in range(n):
    a.append(list(map(str, input().split())))
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == 'W' or a[i][j] == 'G' or a[i][j] == 'B':
#             ok = True
#             continue
#         else:
#             ok = False
#             break
#     if ok == False:
#         break
# if ok:
#     print('#Black&White')
# else:
#     print('#Color')
flag = '#Black&White'
for i in range(n):
    for j in range(m):
        if a[i][j] not in 'BWG':
            flag = '#Color'
            break
    if flag == '#Color':
        break
print(flag)