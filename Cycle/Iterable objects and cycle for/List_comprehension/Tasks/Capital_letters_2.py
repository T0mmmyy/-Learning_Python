from string import ascii_uppercase
n = int(input())
ascii_uppercase = list(ascii_uppercase)
a = [ascii_uppercase[i] * (i + 1) for i in range(n)]
print(a)