my_list = ['banana', 'orange', 'apple', 'mango', 'panapple', 'watermelon']
print('Список фруктов: ', my_list)
print('Первый фрукт: ', my_list[0])
print('Последний фрукт: ', my_list[-1])
print('Фрукты с 3 по 5 ', my_list[2:5])
my_list[2] = 'passion'
print('Измененный список фруктов: ', my_list)
s = ''
print(s)
my_dict = {'banana': 'банан', 'orange': 'Апельсин', 'apple': 'Яблоко', 'mango': 'Манго', 'panapple': 'Ананас',
           'watermellon': 'Арбуз'}
print('Словарь: ', my_dict)
print('Перевод: ', my_dict['banana'])
my_dict['kiwi'] = 'Киви'
del my_dict['orange']
print('Измененный словарь: ', my_dict)
