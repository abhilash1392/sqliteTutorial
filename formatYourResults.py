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

# fetch one
#print(c.fetchone())
# fetch many

#print(c.fetchmany(3))

# fetch all

items=c.fetchall()

for item in items:
    print('First Name:{} |Last Name: {} |Email: {}'.format(item[0],item[1],item[2 ]))

# commit

conn.commit()

# closing the connection

conn.close()
