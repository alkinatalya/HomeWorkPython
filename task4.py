#Напишите программу, которая по заданному номеру четверти, показывает
#диапазон возможных координат точек в этой четверти (x и y).
quarter_number = float(input('Введите номер четверти:'))
if quarter_number > 4:
    print('Такой четверти нет')
elif quarter_number == 1:
    print('x от 0 до +∞ и y от 0 до +∞') 
elif quarter_number == 2:
    print('x от 0 до -∞ и y от 0 до +∞')
elif quarter_number == 3:
    print('x от 0 до -∞ и y от 0 до -∞')
elif quarter_number == 4:
    print('x от 0 до +∞ и y от 0 до -∞')             