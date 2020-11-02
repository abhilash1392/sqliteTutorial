import sqlite3

conn=sqlite3.connect('customer.db')

c=conn.cursor()


# Query the database using and or 

c.execute("SELECT rowid,* from customers where last_name LIKE 'D%' or rowid=5")

items=c.fetchall()

for item in items:
    print(item)

conn.commit()


conn.close()
