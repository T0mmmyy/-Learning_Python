n = int(input())
et = 0
i = 0
count = 0
while True:
    i = i + 1
    et = et + i
    if et <= n:
        n = n - et
        count = count + 1
    else:
        break
print(count)