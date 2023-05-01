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


def insert_survey(data, name, age, gender, inst, who_is_interested):
    cursors.execute("""
    INSERT INTO survey(data, name, age, gender, inst, who_is_interested)
        VALUES (:name, :age, :gender, :inst, :who_is_interested),

    """, {
        'name': data.get('name'),
        'age': data.get('age'),
        'gender': gender,
        'inst': data.get('inst'),
        'who_is_interested': who_is_interested
    })
    bd.commit()


if __name__ == "__main__":
    create_tables()
    insert_survey()
