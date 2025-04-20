import sqlite3

conn = sqlite3.connect('customwear.db')
cursor = conn.cursor()

with open('database/schema.sql') as f:
    cursor.executescript(f.read())

conn.commit()
conn.close()
