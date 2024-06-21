import random

line = int(input('Введите количество строк: '))
column = int(input('Введите количество столбцов: '))
page = int(input('Введите количество страниц: '))
print(f'страница {random.randint(1, page)}, столбец {random.randint(1, column)}, строка {random.randint(1, line)}')
