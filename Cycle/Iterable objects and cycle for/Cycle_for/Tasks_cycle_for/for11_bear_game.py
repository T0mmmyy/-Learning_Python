from random import randint
mishka = 0
cris = 0
n = int(input())
for i in range(n):
    a = randint(1, 6)
    b = randint(1, 6)
    print(a, b)
    if a > b:
        mishka += 1
    elif b > a:
        cris += 1
    else:
        mishka += 0
if mishka > cris:
    print('Mishka')
elif mishka < cris:
    print('Chris')
else:
    print('Friendship is magic!^^')