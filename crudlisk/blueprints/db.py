import sqlite3


def get_cursor():
    conn = sqlite3.connect('instance/database.db')
    cursor = conn.cursor()
    return cursor


def drop_cur_conn(cursor):
    cursor.connection.commit()
    cursor.connection.close()


def register_user(**kw):
    cursor = get_cursor()
    cursor.execute(f"insert into users (username, email,  password) values ('{kw['username']}', '{kw['email']}', '{kw['password']}');")
    drop_cur_conn(cursor)


def get_users():
    cursor = get_cursor()
    users = cursor.execute('select * from users;').fetchall()
    drop_cur_conn(cursor)
    return users

