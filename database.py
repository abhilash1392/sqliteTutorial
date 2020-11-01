import sqlite3 

# For connecting into memory ie; to use only system memory for storing a temporary database 

# conn=sqlite3.connect(:memory:)

# For storing the database 

conn=sqlite3.connect('customer.db')

# create a cusor
c=conn.cursor()

# create a table

# c.execute("""CREATE TABLE customers(
#        first_name text,
#        last_name text,
#        email text)
#        """)

# Datatypes in sqlite
# NULL
# INTEGER
# REAL
# TEXT
# BLOB

# Adding our first entry to 
# c.execute("INSERT INTO customers VALUES('John','Doe','john@work.com')")

# c.execute("INSERT INTO customers VALUES('Mary','Poppins','mary@work.com')")

# Adding many customer to the table in a single command

many_customers=[('Neo','Anderson','neo@work.com'),('Papa','Joe','papa@work.com'),('Mummy','Doe','mummy@work.com')]

c.executemany("INSERT INTO customers VALUES(?,?,?)",many_customers)

print("Command executed successfully....")

# Commit our command

conn.commit()

# close our connection

conn.close()
