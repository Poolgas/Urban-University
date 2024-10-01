'''
Задача "Средний баланс пользователя":
Для решения этой задачи вам понадобится решение предыдущей.
Для решения необходимо дополнить существующий код:
Удалите из базы данных not_telegram.db запись с id = 6.
Подсчитать общее количество записей.
Посчитать сумму всех балансов.
Вывести в консоль средний баланс всех пользователя.
'''

import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')


'''
Заполнение таблицы
'''
def insert_table():
    for i in range(1, 11):
        cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)',
                       (f'User{i}', f'example{i}@gmail.com', f'{i}0', '1000'))


'''Обновление баланса'''
def change_balance():
    for i in range(1, 11):
        if i % 2 != 0:
            cursor.execute('UPDATE Users SET balance = ? WHERE username = ?', (500, f'User{i}'))


'''Удаление каждой 3-ей записи'''
def del_third():
    third = 1
    for i in range(1, 11):
        if i == third:
            cursor.execute('DELETE FROM Users WHERE username = ?', (f'User{i}',))
            third += 3

'''Выборка из Users чей Age != 60  и вывод в консоль'''
def user_formatted():
    cursor.execute('SELECT username, email, age, balance FROM Users WHERE age != ?', (60,))
    users = cursor.fetchall()
    for user in users:
        print(f'Имя: {user[0]} | Почта: {user[1]}  | Возраст: {user[2]} | Баланс: {user[3]}')

def user_del_id():
    cursor.execute('DELETE FROM Users WHERE id =?', (6,))

def total_users():
    cursor.execute('SELECT COUNT(*) FROM Users')
    return cursor.fetchone()[0]

def all_balances():
    cursor.execute('SELECT SUM(balance) FROM Users')
    return cursor.fetchone()[0]

# insert_table()
change_balance()
del_third()
user_formatted()
user_del_id()
print(all_balances()/total_users())

connection.commit()
connection.close()
