'''
2023/11/30 00:00|Домашнее задание по теме "Генераторы"
Цель: более глубоко понять особенности работы с функциями генераторами и оператором yield в Python.

Задача:
Напишите функцию-генератор all_variants(text), которая принимает строку textи возвращает объект-генератор,
при каждой итерации которого будет возвращаться подпоследовательности переданной строки.

Пункты задачи:
 1 Напишите функцию-генератор all_variants(text).
 2 Опишите логику работы внутри функции all_variants.
 3 Вызовите функцию all_variants и выполните итерации.
Пример результата выполнения программы:
Пример работы функции:
a = all_variants("abc")
for i in a:
print(i)
Вывод на консоль:
a
b
c
ab
bc
abc

Примечания:
 1 Для функции генератора используйте оператор yield.
'''


def all_variants(text):
    for index in range(len(text)):
        for i in range(len(text) - index):
            yield text[i:i + index + 1]


a = all_variants('abc')
for i in a:
    print(i)