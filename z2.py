import sqlite3
db = sqlite3.connect('server.db')
cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Tablichka (id INTEGER PRIMARY KEY, login text, password text)''')
cur.execute('''INSERT INTO Tablichka (login, password) VALUES (?,?)''', [input( 'Введите логин: '), input( 'Введите пароль: ')])
db.commit()
cur.close()