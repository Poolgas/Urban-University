"""1st program"""
print(9 ** 0.5 * 5)
"""2nd program"""
print(9.99 > 9.88 and 1000 != 1000.1)
"""3nd program"""
print('2 * 2 + 2 Результат:', 2 * 2 + 2)
print('2 * (2 + 2) Результат:', 2 * (2 + 2))
print('2 * 2 + 2 == 2 * (2 + 2) Результат:', 2 * 2 + 2 == 2 * (2 + 2))
"""4nd program"""
"""Первый метод"""
a = '123.456'
for i in a:
    if i == '.':
        print(a[a.index('.')+1])
"""Второй метод"""
a = float(a) * 10
a = int(a) % 10
print(a)
