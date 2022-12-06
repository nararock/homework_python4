from itertools import count

start_param = int(input("Введите начальное значение: "))
stop_param = int(input("Введите конечное значение: "))
for el in count(start_param):
    if el == int(stop_param + 1):
        break
    print(el)
