n = int(input())
i = 1
a = []
count = 0
while i*i <= n:
    if n % i == 0:
        a.append(i)
        if i != n//i:
            a.append(n//i)
    i +=1
if len(a) == 2:
    print('Yes')
else:
    print('No')