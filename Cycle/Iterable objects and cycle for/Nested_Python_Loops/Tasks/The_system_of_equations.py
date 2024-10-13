n, m = map(int, input().split())
count =  0
for i in range(n+1):
    for x in range(m+1):
        if i ** 2 + x == n and i + x ** 2 == m:
            count += 1
print(count)