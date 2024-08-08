from random import randint
n = int(input())
# sum = 1
# for i in range(1, n + 1):
#     sum = sum * i
# print(sum)
# c = int(input())
# for x in range(c):
#     print('hello')
sum = 0
# for i in range(n):
#     a = randint(1, 100)
#     sum += a
#     print(a, end=' ')
# print()
# print(sum)
for i in range(n):
    a = int(input())
    sum += a
    print('Осталось', n - a)
print('Всего', sum)
print(sum/n)