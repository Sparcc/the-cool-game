import sqlite3
con = sqlite3.connect('sql-data.db')
cur = con.cursor()
cur.execute("SELECT * FROM settings WHERE key = 'testKey'")
print(cur.fetchone()[1])