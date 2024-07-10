n = int(input())
sum = 0
s = 0
schet = int(input())
while True:
    sum = sum + schet
    if sum > n:
        sum = sum - schet
        break
    else:
        s = s + 1
        schet = int(input())
print('Довольно!')
print(sum)
print(s)