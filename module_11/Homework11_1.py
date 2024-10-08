﻿'''Домашнее задание по теме "Обзор сторонних библиотек Python"
Задача:
Выберите одну или несколько сторонних библиотек Python, например, requests, pandas, numpy, matplotlib, pillow.
После выбора библиотек(-и) изучите документацию к ней(ним), ознакомьтесь с их основными возможностями и функциями. К каждой библиотеке дана ссылка на документацию ниже.
Если вы выбрали:
requests - запросить данные с сайта и вывести их в консоль.
pandas - считать данные из файла, выполнить простой анализ данных (на своё усмотрение) и вывести результаты в консоль.
numpy - создать массив чисел, выполнить математические операции с массивом и вывести результаты в консоль.
matplotlib - визуализировать данные с помощью библиотеки любым удобным для вас инструментом из библиотеки.
pillow - обработать изображение, например, изменить его размер, применить эффекты и сохранить в другой формат.
В приложении к ссылке на GitHub напишите комментарий о возможностях, которые предоставила вам выбранная библиотека и как вы расширили возможности Python с её помощью.
Примечания:
Можете выбрать не более 3-х библиотек для изучения.
Желательно продемонстрировать от 3-х функций/классов/методов/операций из каждой выбранной библиотеки.'''

print('Библиотека Requests')
import requests

CBRF = ('https://www.cbr-xml-daily.ru/daily_json.js')
'''Считывание информации о курсах валют с сайта ЦБРФ'''
r = requests.get(CBRF, timeout=1)  # Прекращает ожидание от сервера если сервер не отвечает в течении 1 сек
print(f'\nСтатус ответа от сервера: {r.status_code}')
print(f'\nЗагловки ответа от сервера: {r.headers}')

'''Вывод даты и стоимости валют'''
Date = r.json()['Date']
EUR = r.json()['Valute']['EUR']['Value']
USD = r.json()['Valute']['USD']['Value']
print(f'\nСтоимость валют на {Date} : EUR = {EUR}, USD = {USD}')

print('\nБиблиотека NumPy')
import numpy as np
a = np.array([[1, 8, 5, 4], [5, 4, 3, 9], [12, 10, 11, 13]])
print('\nВывод размерности массива. В данном cлучае 3х4 3 строки и 4 столбца')
print(a.shape)
print('\nСортировка каждой части массива по возрастанию')
print(np.sort(a))
print('\nОбщее количество элементов в массиве')
print(a.size)

b = np.arange(1, 13).reshape(3, 4)
print(f'\nУмножение каждого элемента массива на 10 :\n{b*10}')
print(f'\nМаксимальный элемент массива :{b.max()}')
print(f'\nСумма всех элементов массива :{b.sum()}')

rng = np.random.default_rng()
c = rng.integers(14,size=(3,4))
print(f'\nГенерация масссива с помощью генератора случайных чисел:\n{c}')

print(f'\nСложение двух одинаковых масссивов:\n{a+b}')

