import sqlite3 

# For storing the database 

conn=sqlite3.connect('customer.db')

# create a cusor
c=conn.cursor()

# Querying data and Fetching all

c.execute('SELECT  * FROM customers where last_name like "D%"')

# fetch all

items=c.fetchall()
for item in items:
    print(item)

# commit

conn.commit()

# closing the connection

conn.close()
