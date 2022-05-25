n1 = int(input('Первая оценка :'))
n2 = int(input('Вторая оценка :'))
n3 = int(input('Третья оценка :'))

srf = (n1 + n2 + n3) / 3

if 2 <= srf <= 3:
    print('Троечник')
elif 3 < srf < 4:
    print('надо подтягивать')
elif 4 < srf < 5:
    print('Хорошист')
elif srf == 5:
    print('Отличник')
else:
