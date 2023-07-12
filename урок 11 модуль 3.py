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

def get_users_list(cursor):
    command = """
        SELECT * FROM user
    """
    result = cursor.execute(command)
    print(result)
    users = result.fetchall()
    print(users) 

def update_user(cursor, value, user_id):
    command = """
        UPDATE user 
        SET name = ?
        WHERE id = ?
    """
    cursor.execute(command, (value, user_id))

def delete_users(cursor):
    command = """
        DELETE FROM User
    """
    cursor.execute(command)

def get_user(cursor, name):
    command = """
        SELECT * FROM User
        WHERE name = ?
    """
    result = cursor.execute(command, (name,))
    print(list(result))

with sqlite3.connect("data.db") as cursor:
    create_table_user(cursor) 
    # update_user(cursor, "Никита", 1)
    # get_users_list(cursor)
    delete_users(cursor)
    add_user(cursor, User("Иван", "Иванов", "male"))
    get_user(cursor, "Иван")