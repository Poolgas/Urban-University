import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INT PRIMARY KEY,
title TEXT NO NULL,
description TEXT,
price INT NOT NULL
);
''')

'''
Create функция которая добавляет в БД продукт по ID если его еще не было в БД
'''


def initiate_db(product_id, title, description, price):
    check_product = cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
    if check_product.fetchone() is None:
        cursor.execute(f'''
        INSERT INTO Products VALUES('{product_id}', '{title}', '{description}', '{price}')
        ''')
    connection.commit()


'''
Read функция которая возвращает список словарей созданный с помощью БД
'''


def get_all_products():
    product_list = cursor.execute('SELECT * FROM Products')
    products = {}
    for product in product_list:
        products[product[0]] = product[1], product[2], product[3]
    connection.commit()
    return products


'''
Заполнение SQL таблицы
'''
for i in range(1, 5):
    initiate_db(i, f'Продукт {i}', f'Описание {i}', i * 100)

connection.commit()

