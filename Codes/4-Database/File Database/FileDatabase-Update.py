
import sqlite3
import time

if__name__="__main__"

try:
    con = sqlite3.connect('Database.db') 
    cur = con.cursor()

    #Table should be created already in the Database File.

    cur.execute("UPDATE Employee SET Name='Arslan Haider Sherazi'   WHERE ID='1'")

		
    con.commit()

    cur.execute("SELECT * FROM Employee")
    data=cur.fetchall()

    for row in data:
        print(row)

except sqlite3.Error:

    if con:
        con.rollback()

finally:
		
    if con:
        con.close()






    
