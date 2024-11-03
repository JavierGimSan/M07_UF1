import psycopg2

conn = psycopg2.connect(
    database="postgres",
    user='javier_gimenez',
    password='javi123',
    host='localhost',
    port='5432'
)

connection = conn.cursor()

def elimina_usuari(user_id):
    sql = 'DELETE FROM USERS WHERE user_id = %s;'
    connection.execute(sql, (user_id,))
    conn.commit()