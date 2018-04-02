import mysql.connector
from config import DB_HOST, DB_PORT, DB_USERNAME, DB_PASSWORD, DB_NAME


conn = mysql.connector.connect(
    host=DB_HOST,
    port=DB_PORT,
    user=DB_USERNAME,
    password=DB_PASSWORD,
    database=DB_NAME,
    charset='utf8'
)


def execute_create_or_drop(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    cursor.close()


def execute_insert(conn, sql, param):
    cursor = conn.cursor()
    cursor.execute(sql, param)
    conn.commit()
    cursor.close()


def executemany_insert(conn, sql, params):
    try:
        cursor = conn.cursor()
        cursor.executemany(sql, params)
        conn.commit()
        cursor.close()
        return None
    except mysql.connector.IntegrityError as e:
        return e.msg


def execute_select(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    data = cursor.fetchall()
    cursor.close()
    return data
