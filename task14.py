# Требуется вывести все целые степени двойки (т.е. числа
# вида 2k), не превосходящие числа N.
# 10 -> 1 2 4 8

number = int(input('Введите число: '))
i=0
if number!=0:
    while 2 ** i <=number:
        print(2**i, end=' ')
        i+=1
else:
    print('Ошибка ввода')