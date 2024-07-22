print('Для выхода пропишите exit')
count = 5
while count >= 0:
    a = input()
    if a == 'exit':
        break
    if len(a) < 5:
        print('Ведите больше 5 символов')
        continue
    print('Молодец, давай еще')
    count = count - 1
else:
    print('good')
print('stop')