import sqlite3
'''CREATE TABLE userbase (
                                    id INTEGER PRIMARY KEY,
                                    name TEXT NOT NULL,
                                    baying_date TEXT,
                                    ending_date TEXT,
                                    buyed INTEGER NOT NULL);'''


class Data_Conn:

    def add_user(self, user_id, user_name):
        try:
            conn = sqlite3.connect('tele_data.db')
            cursor = conn.cursor()
            cursor.execute("SELECT id FROM userbase")
            if cursor.fetchone() is None:
                cursor.execute(f"INSERT INTO userbase VALUES (?, ?, ?, ?, ?)", (user_id, user_name, '0', '0', 0))
                conn.commit()
                print('User added')


        except sqlite3.Error as err:
            print("Ошибка при подключении к sqlite", err)
        finally:
            if (conn):
                conn.close()
                print("Соединение с SQLite закрыто")

    def get_rows(self):
        try:
            conn = sqlite3.connect('tele_data.db')
            cursor = conn.cursor()
            for value in cursor.execute("SELECT * FROM userbase"):
                print(value)


        except sqlite3.Error as err:
            print("Ошибка при подключении к sqlite", err)
        finally:
            if (conn):
                conn.close()
                print("Соединение с SQLite закрыто")

db = Data_Conn()
db.add_user(1234567, 'edgar')
db.get_rows()