n = int(input())
g = 0
while g < n:
    print('Hello World')
    g = g + 1
a = [1, 2, 3, 7, 3, 9, 3]
while 3 in a:
    a.remove(3)
print(a)
k = 'privet'
while len(k) > 0:
    print(k[0])
    k = k[1:]
    print(len(k))
h = input('Введите пароль' )
pas = '12345'
count = 0
while h != pas:
    count = count + 1
    print('Неправильный пароль')
    h = input('Введите пароль снова')
print('Пароль верный')
print('Кол-во неправильных попыток: ', count)
x = int(input())
sum = 0
while x != 0:
    sum = sum + x
    x = int(input())
print(sum)