import psycopg2

conn = psycopg2.connect(
    database="postgres",
    user='javier_gimenez',
    password='javi123',
    host='localhost',
    port='5432'
)

connection = conn.cursor()

def actualitza_usuari(user_id, name, surname, age, email):
    sql = '''UPDATE USERS
            SET user_name = %s, user_surname = %s, user_age = %s, user_email = %s
            WHERE user_id = %s;'''
    connection.execute(sql, (name, surname, age, email, user_id))
    conn.commit()

def actualitza_nom(user_id, name):
    sql = '''UPDATE USERS
            SET user_name = %s
            WHERE user_id = %s;'''
    connection.execute(sql, (name, user_id))
    conn.commit()

def actualitza_cognom(user_id, surname):
    sql = '''UPDATE USERS
            SET user_surname = %s
            WHERE user_id = %s;'''
    connection.execute(sql, (surname, user_id))
    conn.commit()

def actualitza_edat(user_id, age):
    sql = '''UPDATE USERS
            SET user_age = %s
            WHERE user_id = %s;'''
    connection.execute(sql, (age, user_id))
    conn.commit()

def actualitza_email(user_id, email):
    sql = '''UPDATE USERS
            SET user_email = %s
            WHERE user_surname = %s;'''
    connection.execute(sql, (email, user_id))
    conn.commit()