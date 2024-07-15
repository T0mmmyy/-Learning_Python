n = int(input())
sov = 7
count = 0
while n > 0:
    last = n % 10
    if sov == last:
        count +=1
    n = n // 10
print(count)