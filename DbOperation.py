import sqlite3
conn = sqlite3.connect('example.db')

c =conn.cursor()

#Create table

c.execute('''CREATE TABLE sample(seq real,date text,waterlevel real,Weather_status text,Weather_humidity real)''')

c.execute("INSERT INTO sample VALUES(1,'2016-09-23',20,'Rain',30)")

conn.commit()

for row in c.execute('SELECT * FROM sample '):
  print row

conn.close()
