n, m = map(int, input().split())
a = []
max_bros = 0
ind = 0
summ = 0
summ1 = 0
for i in range(n):
    b = list(map(int, input().split()))
    a.append(b)

max_bros = max(a[0])
ind = 0
for i in range(n - 1):
    if max_bros < max(a[i + 1]):
        max_bros = max(a[i + 1])
        ind = i + 1
    elif max_bros == max(a[i + 1]) and max(a[ind]) <= max(a[i + 1]):
        # for j in a[ind]:
        #     summ += j
        summ = sum(a[ind])
        summ1 = sum(a[i + 1])
        # for x in a[i + 1]:
        #     summ1 += x
        if summ1 > summ:
            ind = i + 1
print(ind)
# n, m = map(int, input().split())
# a = []
# ind = 0
# for i in range(n):
#     b = list(map(int, input().split()))
#     a.append(b)
# ind = 0
# for i in range(n):
#     sum1 = 0
#     sum2 = 0
#     for x in range(i + 1, n):
#         if max(a[i]) < max(a[x]):
#             if max(a[x]) > max(a[ind]):
#                 ind = x
#                 break
#         elif max(a[i]) == max(a[x]) and max(a[ind]) <= max(a[x]):
#                 for j in a[i]:
#                     sum1 += j
#                 for y in a[i]:
#                     sum2 += y
#                 if sum2 > sum1:
#                     ind = x
# print(ind)
