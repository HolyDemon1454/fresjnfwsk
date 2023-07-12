import sqlite3 

class User:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender

def create_table_user():
    command = """
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY,
        name TEXT,
        surname TEXT,
        gender TEXT)
    """
    cursor.execute(command)

def add_user(cursor, user):
    command = """
    INSERT INTO user(name, surname, gender)
    VALUE(?, ?, ?)
    """
    cursor.execute(command, (user.name, user.surname, user.gender))

with sqlite3.connect("data.db") as cursor:
    create_table_user(cursor) 
    add_user(cursor, User("Иван", "Иванов", "male"))