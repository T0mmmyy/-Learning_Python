n = input()
while len(n) > 0:
    if n[0] == 'a' or n[0] == 'e':
        print('Ага! Нашлась')
        break
    else:
        print('Текущая буква:', n[0])
        n = n[1::]
else:
    print('Распечатали все буквы')