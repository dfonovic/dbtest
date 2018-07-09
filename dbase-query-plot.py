import sqlite3
import datetime
import time
import random
import numpy as np
import matplotlib.pyplot as plt


conn = sqlite3.connect('dfodb.db')
c = conn.cursor()

# def read_from_db():
c.execute('SELECT * FROM sensor')
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

    c.execute("INSERT INTO 'sensor' (time, temp) VALUES (?, ?)",
          (date, temperatura))

    conn.commit()

plt.legend()

plt.show()

#for i in range(20):
#    data_entry()
#    time.sleep(1)


# for x in range(3, 25):

# temperatura = random.randint(30, 40)

# print (temperatura)
#    print (x)

# Insert

# c.execute ("INSERT INTO `sensor` (time, temp) VALUES (datetime('now'), ?)", (temperatura))

# conn.commit()

conn.close()
