# counter.py

import sqlite3

class Counter:
    def __init__(self):
        self.count = 0

    def add(self):
        self.count += 1
        print(f"Животное зарегистрировано. Общее количество: {self.count}")

    def __enter__(self):
        # Создаем базу данных SQLite и таблицу для хранения счетчика
        self.conn = sqlite3.connect("animal_registry.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS counter (count INTEGER)"
        )
        self.conn.commit()

        # Получаем текущее значение счетчика
        self.cursor.execute("SELECT count FROM counter")
        row = self.cursor.fetchone()
        if row:
            self.count = row[0]

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is not None or traceback is not None:
            print("Произошло исключение или ресурс остался открыт.")
            return False

        # Сохраняем текущее значение счетчика в базу данных
        self.cursor.execute("UPDATE counter SET count=?", (self.count,))
        self.conn.commit()

        print("Ресурс успешно закрыт.")
        self.conn.close()
        return True
