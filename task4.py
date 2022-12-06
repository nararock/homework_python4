list1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

dict1 = {}
for el in list1:
    if not dict1.get(el):
        dict1[el] = 1
    else:
        dict1[el] = dict1.get(el) + 1
list2 = [el[0] for el in dict1.items() if el[1] == 1]
print(list2)


