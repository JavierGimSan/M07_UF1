import psycopg2

conn = psycopg2.connect(
    database="postgres",
    user='javier_gimenez',
    password='javi123',
    host='localhost',
    port='5432'
)

connection = conn.cursor()

def crear_usuari(name, surname, age, email):
    sql = '''INSERT INTO USERS (
                    user_name,
                    user_surname,
                    user_age,
                    user_email
    ) VALUES (?, ?, ?, ?)'''
    connection.execute(sql, (name, surname, age, email))
    conn.commit()