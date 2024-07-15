n = int(input())
last = 0
sum = 0
while n > 0:
    last = n % 10
    sum = sum + last
    n = n // 10
print(sum)