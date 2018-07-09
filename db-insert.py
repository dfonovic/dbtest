import sqlite3
import datetime
import time
import random

conn = sqlite3.connect('sensor.db')
c = conn.cursor()

def read_from_db():
    c.execute('SELECT * FROM log')
    data = c.fetchall()
    print(data)
    for row in data:
        print(row)

def data_entry():

    unix = int(time.time())
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    temperatura = random.randint(30,40)

    print (date)
    print (temperatura)

    c.execute("INSERT INTO 'log' (time, temp) VALUES (?, ?)",
          (date, temperatura))

    conn.commit()
    
for i in range (20):
	data_entry()
	time.sleep(2)
	
conn.close()
