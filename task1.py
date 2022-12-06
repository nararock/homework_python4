from sys import argv

task1_name, number_hours, rate, prize = argv

print(f'Заработная плата сотрудника: '
      f'{int(number_hours) * float(rate) + float(prize)}')

