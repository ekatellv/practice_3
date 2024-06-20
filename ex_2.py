number = int(input('Введите число в диапазоне от 1 до 86400:'))
hours = number//(60**2)
minutes = (number-hours*60**2)//60
seconds = number - hours*60**2 - minutes*60
print(f'{hours} часов {minutes} минут {seconds} секунд')
