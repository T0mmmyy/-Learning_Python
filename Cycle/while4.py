n = int(input())
last = 0
pro = 1
while n > 0:
    last = n % 10
    pro = pro * last
    n = n // 10
print(pro)