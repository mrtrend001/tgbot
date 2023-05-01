import sqlite3
from pathlib import Path

DB_NAME = 'db.sqlite'  # .sqlite, .db
DB_PATH = Path(__file__).parent.parent
bd = sqlite3.connect(DB_PATH / DB_NAME)
cursors = bd.cursor()


def create_tables():
    cursors.execute("""
    CREATE TABLE IF NOT EXISTS survey(
        survey_id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        gender TEXT,
        inst TEXT,
        who_is_interested TEXT
    )""")
    bd.commit()


def insert_survey(data):
    cursors.execute("""
    INSERT INTO survey(name, age, gender, inst, who_is_interested)
        VALUES (:name, :age, :gender, :inst, :who_is_interested)
    """, {
        'name': data['name'],
        'age': data['age'],
        'gender': data['gender'],
        'inst': data['inst'],
        'who_is_interested': data['who_is_interested']
    })
    bd.commit()


if __name__ == "__main__":
    create_tables()
