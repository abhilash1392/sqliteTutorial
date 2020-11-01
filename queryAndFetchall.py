import sqlite3 

conn=sqlite3.connect('customers.db')

import sqlite3 

# For connecting into memory ie; to use only system memory for storing a temporary database 

# conn=sqlite3.connect(:memory:)

# For storing the database 

conn=sqlite3.connect('customer.db')

# create a cusor
c=conn.cursor()

# Querying data and Fetching all

c.execute('SELECT * FROM customers')

# fetch all

print(c.fetchall())

# commit

conn.commit()

# closing the connection

conn.close()
