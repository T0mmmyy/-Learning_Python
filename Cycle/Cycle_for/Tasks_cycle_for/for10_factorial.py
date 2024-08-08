n = int(input())
fa = 1
for i in range(n):
    fa += fa * i
print(fa)