from functools import reduce

my_list = [el for el in range(100, 1001, 2)]

print(my_list)
print(reduce(lambda x, y: x * y, my_list))
