a = [2, 6, 8, 3, 9, 4]
last =  0
while len(a) > 0:
    last = a.pop()
    if last % 2 != 0:
        print('Число ', last, ' из списка a  не четное')
    else:
        print('Число ', last, ' из списка a четное')