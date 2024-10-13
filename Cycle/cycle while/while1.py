x = int(input())
kol = 0
kol_ch = 0
sum = 0
pro = 1
b = 0
m = 999
while x > 0:
    last = x % 10
    kol = kol + 1
    sum = sum + last
    pro = pro * last
    if last % 2 == 0:
        kol_ch += 1
    if last > b:
        b = last
    if last < m:
        m = last
    x = x // 10
print('Всего цифр: ', kol)
print('Всего четных цифр: ', kol)
print('Сумма всех числе: ', sum)
print('Произведение всех числе: ', pro)
print('Самое большое число: ', b)
print('Самое маленькое число: ', m)