import sqlite3

class dataBase:
    def __init__(self):
        self.connector = sqlite3.connect("database/data.db")
        self.cursor = self.connector.cursor()

    def getData(self):
        self.cursor.execute("SELECT * FROM productos")
        datos = self.cursor.fetchall()
        return datos
