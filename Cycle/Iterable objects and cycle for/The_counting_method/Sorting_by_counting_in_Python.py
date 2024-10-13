# # n = list(map(int, input().split()))
# n = list(map(int, input().split()))
# f = [0] * (max(n) + 1)
# for i in n:
#     f[i] += 1
# print(f)
# for i in range(max(n) + 1):
#     if f[i] > 0:
#         print((str(i) + ' ') * f[i], end='')
# s = "jhdf HG jgkfYGg jhgkdf 543 *(^$&*#"
# letters = [0] * 26
# for i in s.lower():
#     if i > 'a' and i < 'z':
#         nomer = ord(i) - 97
#         letters[nomer] += 1
# for i in range(26):
#     if letters[i] > 0:
#         print(chr(i + 97) * letters[i], end='')
n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    for x in range(n - 1 - i):
        if a[x] > a[x +  1]:
            a[x], a[x + 1] = a[x + 1], a[x]
print(*a)