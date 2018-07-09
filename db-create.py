import sqlite3
conn = sqlite3.connect('sensor.db')

c = conn.cursor()

# Create table
c.execute(" CREATE TABLE `log` (`id`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,	`time`	NUMERIC NOT NULL,	`temp`	REAL NOT NULL)")

conn.commit()
