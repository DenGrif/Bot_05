import sqlite3

# Инициализация базы данных и создание таблиц
def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Создание таблицы Products
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        description TEXT NOT NULL,
                        price INTEGER NOT NULL
                    )''')

    # Создание таблицы Users
    cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL,
                        email TEXT NOT NULL,
                        age INTEGER NOT NULL,
                        balance INTEGER NOT NULL DEFAULT 1000
                    )''')

    conn.commit()
    conn.close()

# Получаем все продукты из базы данных
def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()

    conn.close()
    return products

# Добавление нового продукта в таблицу Products
def add_product(title, description, price):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)", (title, description, price))
    conn.commit()
    conn.close()

# Добавление нового пользователя в таблицу Users
def add_user(username, email, age):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (username, email, age, 1000))
    conn.commit()
    conn.close()

# Проверка, существует ли пользователь в базе данных
def is_included(username):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    user = cursor.fetchone()
    conn.close()

    return user is not None

# Удаление пользователя по имени
def delete_user(username):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Проверяем, существует ли пользователь
    cursor.execute("SELECT * FROM Users WHERE username = ?", (username,))
    user = cursor.fetchone()

    if user:
        # Если существует - удаляем его
        cursor.execute("DELETE FROM Users WHERE username = ?", (username,))
        conn.commit()
        print(f"Пользователь {username} был успешно удалён.")
    else:
        print(f"Пользователь {username} не найден.")

    conn.close()

# # Заполяем базу данных
# def fill_products():
#     add_product("Игра 1", "Небольшая игра", 1000)
#     add_product("Игра 2", "Средняя игра", 2000)
#     add_product("Игра 3", "Большая игра", 3000)
#     add_product("Игра 4", "Очень большая игра", 4000)
#     print("Таблица Products успешно заполнена.")
#
#
# # Запускаем и заполяем базу данных
# initiate_db()
# fill_products()
