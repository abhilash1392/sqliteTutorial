import sqlite3 

# For storing the database 

conn=sqlite3.connect('customer.db')

# create a cusor
c=conn.cursor()
# Update Name from John to Jane for row id 1
c.execute("""UPDATE customers SET first_name = 'Jane' WHERE rowid=1""")
# Querying data and Fetching all

c.execute('SELECT  * FROM customers ')

# fetch all

items=c.fetchall()
for item in items:
    print(item)

# commit

conn.commit()

# closing the connection

conn.close()
