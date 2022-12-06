def fact(n):
    generator = (param for param in range(1, n + 1))
    temp = 1
    for elem in generator:
        temp *= elem
        yield temp


amount = int(input("Введите желаемое количество факториалов: "))
for el in fact(amount):
    print(el)
