import sqlite3
import datetime


class DataConn:

    def add_user(self, user_id, user_name):
        try:
            conn = sqlite3.connect('user.db')
            cursor = conn.cursor()
            b = False
            for values in cursor.execute("SELECT id FROM userbase"):
                if user_id == values[0]:
                    b = True
            if not b:
                cursor.execute(f"INSERT INTO userbase VALUES (?, ?, ?, ?, ?)", (user_id, user_name, '0', '0', 0))
                conn.commit()
        except sqlite3.Error as e:
            print(repr(e))
        finally:
            conn.close()

    def get_expire(self):
        try:
            conn = sqlite3.connect('user.db')
            cursor = conn.cursor()
            dates = []
            for i in cursor.execute(f"SELECT ending_date, id FROM userbase "):
                dates.append(i)
            conn.commit()
            return dates
        except sqlite3.Error as e:
            print(repr(e))
        finally:
            conn.close()

    def get_rows(self):
        try:
            conn = sqlite3.connect('user.db')
            cursor = conn.cursor()
            userlist = []
            for value in cursor.execute("SELECT * FROM userbase"):
                userlist.append(value)
            return userlist
        except sqlite3.Error as e:
            print(repr(e))
        finally:
            conn.close()

    def set_time(self, user_id, start_time, end_time):
        try:
            conn = sqlite3.connect('user.db')
            cursor = conn.cursor()
            print(start_time)
            print(end_time)
            cursor.execute(
                f"UPDATE userbase SET baying_date = ?,ending_date = ?, buyed = ? WHERE id = ?", (start_time, end_time, 1, user_id))
            conn.commit()
        except sqlite3.Error as e:
            print(repr(e))
        finally:
            conn.close()

    def delete(self, user_id):
        try:
            conn = sqlite3.connect('user.db')
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM userbase WHERE id = {user_id}")
            conn.commit()
        except sqlite3.Error as e:
            print(repr(e))
        finally:
            conn.close()

    def create_table(self):
        try:
            conn = sqlite3.connect('user.db')
            cursor = conn.cursor()
            cursor.execute(
                "CREATE TABLE userbase ( id BIGINT PRIMARY KEY, name TEXT NOT NULL, baying_date TEXT, ending_date TEXT, buyed INTEGER NOT NULL)")
            conn.commit()
        except sqlite3.Error as e:
            print(repr(e))
        finally:
            conn.close()

    def week_plan(self, user_id):
        today_date = datetime.datetime.now().date()
        expire_date = today_date + datetime.timedelta(weeks=1)
        self.set_time(user_id=user_id,
                      start_time=str(today_date.isoformat()),
                      end_time=str(expire_date.isoformat()))

    def mouth_plan(self, user_id):
        today_date = datetime.datetime.now().date()
        expire_date = today_date + datetime.timedelta(weeks=4)
        self.set_time(user_id=user_id,
                      start_time=str(today_date.isoformat()),
                      end_time=str(expire_date.isoformat()))

    def command(self, command):
        try:
            conn = sqlite3.connect('user.db')
            cursor = conn.cursor()
            print(cursor.execute(command))
            conn.commit()
        except sqlite3.Error as e:
            print(repr(e))
        finally:
            conn.close()

