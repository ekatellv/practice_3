X, Y, N = map(int, input('Введите стоимость латте в рублях и копейках и количество заказов через пробел:').split())
income_cents = Y*N
income_rub = (X*N)+(income_cents//100)
print(f'{income_rub} руб. {income_cents%100} коп.')
