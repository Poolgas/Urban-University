def print_params(a=1, b='string', c=True):
    print(a, b, c)


print('1.Функция с параметрами по умолчанию')
print_params()
print_params(64, 213)
print_params(b=25)
print_params(c=[1, 2, 3])

print('')
print('2.Распаковка параметров')
values_list = [32, '454', [239, 81, 324]]
values_dict = {'a': 64, 'b': '545', 'c': [72, 366, 521]}
print_params(*values_list)
print_params(**values_dict)

print('')
print('3.Распаковка + отдельные параметры')
values_list_2 = [True, 'Другой тип']
print_params(*values_list_2, 42)
