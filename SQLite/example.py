import sqlite3

connect = sqlite3.connect('instance.db')
cursor = connect.cursor()
cursor.execute('CREATE TABLE table_1 (id INTEGER PRIMARY KEY, firstname VARCHAR(20), lastname VARCHAR(30))')
connect.commit()
for i in range(0,13):
    cursor.execute('INSERT INTO table_1 (id, firstname,lastname ) VALUES(NULL, "darion-%d","yaphet-%d")'%(i,i))
connect.commit()
print cursor.lastrowid

#cursor.execute('SELECT * FROM table_1')
#print cursor.fetchall()
