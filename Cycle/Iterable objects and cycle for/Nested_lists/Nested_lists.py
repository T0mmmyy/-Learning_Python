a = [
    [0, 2, 4, 6],
     [1, 5, 9, 13],
     [3, 10, 17, 19]
]
# print(len(a))
# print(a[2][2][1])
# b = ['hello', 'hi', 'world']
# print(b[2][-1])
# for i in a:
#     for x in i:
#         print(x, end=' ')
#     print()
# for j in range(4):
#     for i in range(3):
#         print(a[i][j], end=' ')
#     print()
# for i in range(2, -1, -1):
#     for j in range(3, -1, -1):
#         print(a[i][j], end=' ')
#     print()
# for i in range(len(a)):
#     sum = 0
#     for x in range(4):
#         sum += a[i][x]
#     print(sum)
a = []
n = int(input()) #строка
# m = int(input()) #столбцов
# for i in range(n):
#     b = []
#     for x in range(m):
#         b.append(int(input()))
#     a.append(b)
# for j in a:
#     print(j)
for i in range(n):
    a.append([0] * n)
for i in range(n):
    for x in range(n):
        if i == x:
            a[i][x] = 10
        elif i < x:
            a[i][x] = 5
        else:
            a[i][x] = 3
for x in a:
    print(x)