b = int(input())
a = int(input())
while a >= b:
    if b % 777 == 0:
        break
    if b % 2 == 0 or b % 3 == 0:
        b += 1
        continue
    print(b)
    b += 1