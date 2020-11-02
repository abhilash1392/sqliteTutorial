import sqlite3

# Query all results

def show_all():
    conn=sqlite3.connect('customer.db')
    c=conn.cursor()
    c.execute("SELECT * FROM customers")
    items=c.fetchall()
    for item in items:
        print(item)

    conn.commit()
    conn.close()
    
