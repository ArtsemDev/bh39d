from sqlite3 import connect


conn = connect('db.sqlite3')
cur = conn.cursor()

# Category
# name STR
# Product
# name STR price FLOAT descr STR model manufacture image characteristics category

cur.execute('''
    CREATE TABLE IF NOT EXISTS category (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (24) NOT NULL UNIQUE
);
''')
conn.commit()


cur.execute('''
    CREATE TABLE IF NOT EXISTS product (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (128) NOT NULL,
        price DECIMAL (8, 2) NOT NULL CHECK ( price > 0 ),
        model VARCHAR (128),
        category_id INTEGER NOT NULL CHECK ( category_id > 0 ),
        FOREIGN KEY (category_id) REFERENCES category (id) ON DELETE RESTRICT
    );
''')
conn.commit()

# cur.execute('CREATE UNIQUE INDEX category_id_index ON product (category_id);')
# cur.execute('CREATE UNIQUE INDEX is_published_index ON product (is_published);')
# conn.commit()
# DROP TABLE product;  -  удаление таблицы
# ALTER TABLE - изменение таблицы (добавление/удаление/изменение атрибутов)
#
# SQL Injection
# BAD PRACTICE
# text = input()
# cur.execute(f'''
#     INSERT INTO category (name) VALUES ('{text}');
# ''')
#
# cur.executemany('''
#     INSERT INTO category (name) VALUES (?);
# ''', (('Sandwich', ), ('Milkshake', )))
# conn.commit()
#
# cur.execute('''
#     DELETE FROM category WHERE name LIKE ? or id > ?;
# ''', (2, '%скидка%'))
# conn.commit()

# cur.execute('''
#     UPDATE category SET name = ? WHERE id = ?;
# ''', ('Кофе', 1))
# conn.commit()

# cur.execute('''
#     SELECT category.id, category.name FROM category ORDER BY category.id DESC;
# ''')
# print(cur.fetchall())
#
# cur.executemany('''
#     INSERT INTO product (name, price, model, category_id) VALUES (?, ?, ?, ?);
# ''', (('Latte', 5.5, 'With Milk', 1), ('Grill', 7, 'With pork', 1)))
# conn.commit()

# cur.execute('''
#     SELECT category.name, product.name, product.price
#     FROM category
#     JOIN product
#     ON category.id = product.category_id
#     WHERE product.price > 6
#     ORDER BY product.price DESC;
# ''')
# print(cur.fetchall())
