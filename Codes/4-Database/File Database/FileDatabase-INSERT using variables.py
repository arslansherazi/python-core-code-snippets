
import sqlite3
import time

def Database(name,idd,contact):

    try:
        con = sqlite3.connect('Database.db') 

        
    
        cur = con.cursor()

          
        cur.execute("CREATE TABLE IF NOT EXISTS Employee(ID INT, Name TEXT,CotactNo INT)") #This query checks that whether the table already exist in the database.
        #if so then it does not create new table.and if table exists then it creates the table.It means that table is created just once then
        #all the entries are gone to the same table.

        cur.execute("INSERT INTO Employee VALUES(?, ?, ?)",(idd,name,contact))

		
        con.commit()
        cur.execute("SELECT * FROM Employee")
        data = cur.fetchall()
		
        for row in data:
            print(row)

    except sqlite3.Error:

        if con:
            con.rollback()

    finally:
		
        if con:
            con.close()

if__name__="__main__"

while True:
    n=input("Enter Name::")
    i=input("Enter Idd::")
    c=input("Enter Contact No::")
    print("\n\nRecord Successfully Stored......\n\n")
    Database(n,i,c)
    print("\n\n")

    time.sleep(3)

    


    
