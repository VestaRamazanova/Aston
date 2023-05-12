number = input('Введите целое число: ')
try:
    if int(number) > 7:
        print('Привет')
    else:
        print('Введенное число <=7')
except ValueError:
    print('Введено не корректное значение')