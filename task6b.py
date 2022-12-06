from itertools import cycle
import keyboard

print("Чтобы остановить цикл нажмите клавишу 'пробел'(space).")
my_string = input("Введите элементы через пробел: ")

mylist = my_string.split()
for el in cycle(mylist):
    if keyboard.is_pressed('space'):
        break
    else:
        print(el)
