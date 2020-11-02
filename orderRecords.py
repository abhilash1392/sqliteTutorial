import sqlite3

conn=sqlite3.connect('customer.db')

c=conn.cursor()


# Query the database order by 

c.execute("SELECT * from customers ORDER BY first_name DESC")

items=c.fetchall()

for item in items:
    print(item)

conn.commit()


conn.close()
