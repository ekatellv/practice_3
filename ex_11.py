import math

n = float(input('Введите угол: '))
hours = math.floor(n / 30)
minutes_angle = n * 12
minutes = (minutes_angle // 6)
minutes_1 = 0
if minutes_angle >= 360:
    minutes_1 = (minutes_angle // 6) % 60
    print(f'Прошло полных {hours} ч. и {minutes_1} мин.')
else:
    print(f'Прошло полных {hours} ч. и {minutes} мин.')
