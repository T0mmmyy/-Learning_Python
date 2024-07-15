n = int(input())
min = 999
max = 0
while n > 0:
    last = n % 10
    if min > last:
        min = last
    if max < last:
        max = last
    n = n // 10
print(min)
print(max)