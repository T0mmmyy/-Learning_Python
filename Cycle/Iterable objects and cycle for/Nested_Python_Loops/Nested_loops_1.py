# for i in range(1, 4):
#     for x in range(10,13):
#         print(i,x)
# from string import printable
# pas = input('Введите пароль из 4 символов ')
# count = 0
# for b1 in printable:
#     for b2 in printable:
#         for b3 in printable:
#             for b4 in printable:
#                 cd = b1+b2+b3+b4
#                 count += 1
#                 if cd == pas:
#                     print('Ваш пароль:', cd)
#                     print('Число попыток за которе удалось его отгадать:', count)
#                     input()
# for i in range(1,10):
#     for x in range(1,11):
#         print(i, '*', x, '=', i*x, end=' ')
#     print()

# slovo = 'tukva'
# # co = 0
# # for b1 in slovo:
# #     for b2 in slovo:
# #         for b3 in slovo:
# #             for b4 in slovo:
# #                 for b5 in slovo:
# #                     for b6 in slovo:
# #                         result = b1+b2+b3+b4+b5+b6
# #                         if result[0] in 'tkv' and result[-1] in 'tkv':
# #                             if result.count('a') + result.count('u'):
# #                                 co += 1
# # print(co)
# for i in range(1, 10001):
#     s = 0
#     n = i
#     while n > 0:
#         s += n % 10
#         n //= 10
#     print(i, s)
count = 0
for i in range(1000, 10000):
    s = 0
    n = i
    while n > 0:
        s += n % 10
        n //= 10
    if s == 20:
        print(i)
        count += i
print(count)
