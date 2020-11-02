import sqlite3 

# For storing the database 

conn=sqlite3.connect('customer.db')

# create a cusor
c=conn.cursor()
# Delete the name record of the person with rowid 4 
c.execute("""DELETE from customers WHERE rowid =4""")
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
