import psycopg2

conn = psycopg2.connect(
    database="postgres",
    user='javier_gimenez',
    password='javi123',
    host='localhost',
    port='5432'
)

connection = conn.cursor()

def llegir_usuari():
    sql = 'SELECT * FROM USERS;'
    connection.execute(sql)
    conn.commit()