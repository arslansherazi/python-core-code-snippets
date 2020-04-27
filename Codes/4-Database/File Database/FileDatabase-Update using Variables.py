
import sqlite3
import time

def database(name,idd):


    try:
        con = sqlite3.connect('Database.db') 
        cur = con.cursor()

        #Table should be created already in the Oracle Database.

        cur.execute("UPDATE Employee  SET Name=:1   WHERE ID=:2",(name,idd))

		
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

if__name__="__main__"

n=input("Enter Name to be changed::")
i=input("Enter ID for which Name to be changed::")
database(n,i)

time.sleep(2)

print("\nSuccessfully change the ID\n\n")





    
