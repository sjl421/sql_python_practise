import mysql.connector
from config import DB_HOST, DB_PORT, DB_USERNAME, DB_PASSWORD, DB_NAME


class DB(object):

    def __init__(self):
        self.conn = mysql.connector.connect(
            host=DB_HOST,
            port=DB_PORT,
            user=DB_USERNAME,
            password=DB_PASSWORD,
            database=DB_NAME,
            charset='utf8'
        )

    def execute_create_or_drop(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        cursor.close()

    def execute_insert(self, sql, param):
        cursor = self.conn.cursor()
        cursor.execute(sql, param)
        self.conn.commit()
        cursor.close()

    def executemany_insert(self, sql, params):
        try:
            cursor = self.conn.cursor()
            cursor.executemany(sql, params)
            self.conn.commit()
            cursor.close()
            return None
        except mysql.connector.IntegrityError as e:
            return e.msg

    def execute_select_all(self, sql):
        cursor = self.conn.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        return data

    def __del__(self):
        self.close()

    def close(self):
        self.conn.close()
