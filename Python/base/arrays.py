# Базовые приемы работы с массивами

vals = []                       # создаем неопределенный массив

tmp = [[1, 2, 3], 5]            # добавим данные во временный массив
vals.append(tmp)                # добавим элемент в массив через временный массив

vals.append([[1, 2, 3], 5])     # добавим элемент в массив на прямую

print(vals[0])