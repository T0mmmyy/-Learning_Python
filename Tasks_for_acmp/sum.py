n = int(input())
count = 0
if n > 0:
    for i in range(n+1):
        count += i
    print(count)
else:
    for i in range(1, n-1, -1):
        count += i
    print(count)