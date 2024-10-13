from string import ascii_uppercase
n = int(input())
ascii_uppercase = list(ascii_uppercase)
a = [ascii_uppercase[i] for i in range(n)]
print(a)