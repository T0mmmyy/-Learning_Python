n = int(input())
last = 0
while n > 0:
    last = n % 10
    n = n // 10
    print(last)