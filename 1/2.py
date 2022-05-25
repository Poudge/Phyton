name1 = 'Вася'
name2 ='Кузя'

name1, name2 = name2, name1

#if условие правда:
#  команда1
#elif условие2 правда:
#  команды2
#else
#  команды3

n1 = input("1 оценка")
n2 = input("2 оценка")
n3 = input("3 оценка")
srf = (int(n1) + int(n2) + int(n3) ) / 3

if 2 < srf <= 3:
    ptint  ('Фу двоечник')
elif 3< srf <= 4:
    print('почти абоба')
elif 4 < srf < 5:
    print('хорошист')
elif srf == 5:
    print('ботан')
else:
    print('введи правильны оценки')
