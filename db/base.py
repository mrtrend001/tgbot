import sqlite3
from pathlib import Path

DB_NAME = 'db.sqlite'  # .sqlite, .db
DB_PATH = Path(__file__).parent.parent
db = sqlite3.connect(DB_PATH / DB_NAME)
cursor = db.cursor()


def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS survey(
        survey_id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        gender TEXT,
        inst TEXT,
        who_is_interested TEXT
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS products(
            product_id INTEGER PRIMARY KEY,
            name TEXT,
            price INTEGER,
            photo TEXT
        )""")
    db.commit()


def insert_survey(data):
    cursor.execute("""
    INSERT INTO survey(name, age, gender, inst, who_is_interested)
        VALUES (:name, :age, :gender, :inst, :who_is_interested)
    """, {
        'name': data['name'],
        'age': data['age'],
        'gender': data['gender'],
        'inst': data['inst'],
        'who_is_interested': data['who_is_interested']
    })
    db.commit()



def delete_products():
    cursor.execute("""DROP TABLE IF EXISTS products""")
    db.commit()


def insert_products():
    cursor.execute("""INSERT INTO products(name, price, photo)
        VALUES ('Метровая пицца (Pizza al metro или Pizza alla Palla)',  2700, 'images/1.jpg'),
        ('Сицилийская пицца (Pizza Siciliana)',  550, 'images/2.jpg')
    """)
    db.commit()


def get_products():
    data = cursor.execute("""SELECT * FROM products""")
    return data.fetchall()


def insert_survey(data):
    cursor.execute("""
    INSERT INTO survey(name, age, gender, user_id)
        VALUES ('Daniel', 19, 'male', 12312),
        ('Igor', 30, 'male', 232323)
    """)
    cursor.execute("""
    INSERT INTO survey(name, age, gender, user_id)
        VALUES (:name, :age, :gender, :user_id),

    """, {
        'name': data['name'],
        'age': data['age'],
        'gender': data['gender'],
        'user_id': data['user_id']
    })
    db.commit()


if __name__ == "__main__":
    create_tables()
    insert_products()
    get_products()




