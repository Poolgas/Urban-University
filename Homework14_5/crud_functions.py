import sqlite3

with sqlite3.connect('database.db') as db:
    cursor = db.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Products(
    id INT PRIMARY KEY,
    title TEXT NO NULL,
    description TEXT,
    price INT NO NULL
    );
    ''')

    '''
    Create функция которая добавляет в БД продукт по ID если его еще не было в БД и создает новую таблицу Users
    '''


    def initiate_db(product_id, title, description, price):
        check_product = cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
        if check_product.fetchone() is None:
            cursor.execute(f'''
            INSERT INTO Products VALUES('{product_id}', '{title}', '{description}', '{price}')
            ''')
        cursor.execute('''
                CREATE TABLE IF NOT EXISTS Users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NO NULL,
                email TEXT NO NULL,
                age INT NO NULL,
                balance INT NO NULL
                );
                ''')
        db.commit()


    '''
    Добавляет в БД Users нового пользователяs
    '''


    def add_user(username, email, age, balance=1000):
        cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES(?, ?, ?, ?)',
                       (username, email, age, balance)
                       )
        db.commit()


    '''
    Проверяет в таблице Users есть ли пользователь c переданным именем  
    '''


    def is_included(username):
        check_user = cursor.execute('SELECT * FROM Users WHERE username = ?', (str(username),))
        if check_user.fetchone() is not None:
            return True
        else:
            return False


    '''
    Read функция которая возвращает список словарей созданный с помощью БД
    '''


    def get_all_products():
        product_list = cursor.execute('SELECT * FROM Products')
        products = {}
        for product in product_list:
            products[product[0]] = product[1], product[2], product[3]
        db.commit()
        return products


    '''
    Заполнение SQL таблицы
    '''
    for i in range(1, 5):
        initiate_db(i, f'Продукт {i}', f'Описание {i}', i * 100)

    db.commit()
