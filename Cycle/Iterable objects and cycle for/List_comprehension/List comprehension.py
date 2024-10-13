import random
# название = [выражение for i in коллекция]
# название = [выражение for i in коллекция if условие]
# a = list(map(int, input().split()))
# a = [i for i in a if i % 2 == 0]
# print(*a)
# n = int(input())
# a = [[0] * n for i in range(n)]
# for i in range(n):
#     print(*a[i])
# a = [random.randint(0,11) for i in range(4)]
# b = [random.randint(0,11) for i in range(4)]
# c = [i * j for i in a for j in b if i * j > 10]
# print(*c)
a = [str(i) for i in range(11)]
password = '561'
b = [i + j + h for i in password for j in password for h in password if i + j + h == '561']
print(b)