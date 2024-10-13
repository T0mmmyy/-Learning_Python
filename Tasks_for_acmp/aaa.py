pol = input('Здравствуйте, как ваши дела? ')
if 'хорош' in pol or 'отлично' in pol or 'замечат' in pol or 'норм' in pol or 'крут' in pol:
    print('Это очень хорошо :)')
elif 'плох' in pol or 'ужас' in pol or 'не очень' in pol or 'так себе' in pol:
    print('Ничего, скоро всё наладится :)')
else:
    print('Извините, я вас не понимаю :(')