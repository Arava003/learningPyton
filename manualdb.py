import sqlite3


connect = sqlite3.connect("himeworking.db")
cursor = connect.cursor()

cursor.execute(f'create table humans (name text, password text, info text)')

connect.commit()
connect.close()