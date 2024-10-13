n = int(input())
i = 1
a = []
sum = 0
while i*i <= n:
    if n % i == 0:
        a.append(i)
        sum = sum + i
        if i != n//i:
            a.append(n//i)
            sum = sum + n // i
    i +=1
a.sort()
print(sum)