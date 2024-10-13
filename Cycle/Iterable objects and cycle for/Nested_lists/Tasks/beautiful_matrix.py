# n = []
# count = 0
# for i in range(5):
#     b = list(map(int, input().split()))
#     n.append(b)
# for i in range(5):
#     for x in range(5):
#         if n[i][x] == 1:
#
#             while i != 2 or x != 2:
#                 if i < 2:
#                     n[i + 1][x], n[i][x] = n[i][x], n[i + 1][x]
#                     i += 1
#                     count += 1
#                 elif i > 2:
#                     n[i - 1][x], n[i][x] = n[i][x], n[i - 1][x]
#                     i -= 1
#                     count += 1
#                 else:
#                     while x != 2:
#                         if x < 2:
#                             n[i][x + 1], n[i][x] = n[i][x], n[i][x + 1]
#                             x += 1
#                             count += 1
#                         elif x > 2:
#                             n[i][x - 1], n[i][x] = n[i][x], n[i][x - 1]
#                             x -= 1
#                             count += 1
# print(count)
n = []
ok = True
count = 0
for i in range(5):
    b = list(map(int, input().split()))
    n.append(b)
for i in range(5):
    if ok:
        pass
    else:
        break
    for x in range(5):
        if ok:
            pass
        else:
            break
        if n[i][x] == 1:
            while i != 2 or x != 2:
                if i < 2:
                    n[i + 1][x], n[i][x] = n[i][x], n[i + 1][x]
                    i += 1
                    count += 1
                elif i > 2:
                    n[i - 1][x], n[i][x] = n[i][x], n[i - 1][x]
                    i -= 1
                    count += 1
                else:
                    while x != 2:
                        if x < 2:
                            n[i][x + 1], n[i][x] = n[i][x], n[i][x + 1]
                            x += 1
                            count += 1
                        elif x > 2:
                            n[i][x - 1], n[i][x] = n[i][x], n[i][x - 1]
                            x -= 1
                            count += 1
            ok = False
print(count)