import sqlite3
from pathlib import Path


def init_db():
    DB_NAME = 'db.sqlite'  # .sqlite, .db
    DB_PATH = Path(__file__).parent.parent
    db = sqlite3.connect(DB_PATH / DB_NAME)
    cursor = db.cursor()
    global db, cursor


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
    db.commit()


def insert_survey(data, name, age, gender, inst, who_is_interested):
    cursor.execute("""
    INSERT INTO survey(data, name, age, gender, inst, who_is_interested)
        VALUES (:name, :age, :gender, :inst, :who_is_interested),

    """, {
        'name': data.get('name'),
        'age': data.get('age'),
        'gender': gender,
        'inst': data.get('inst'),
        'who_is_interested': who_is_interested
    })
    db.commit()


if __name__ == "__main__":
    init_db()
    create_tables()
    insert_survey()
