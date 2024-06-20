import math

a, b, c = map(int, input('Введите стороны:').split())
if a + b > c and a + c > b and b + c > a:
    angle_1 = math.acos((a ** 2 + b ** 2 - c ** 2) / (2 * a * b))
    angle_2 = math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c))
    angle_3 = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))
else:
    print('Введите значения, удовлетворящие неравенству теругольника:')
print(math.degrees(angle_1), math.degrees(angle_2), math.degrees(angle_3), sep='\n')
