
import sqlite3
import time

def database(idd):


    try:
        con = sqlite3.connect('Database.db') 
        cur = con.cursor()

        #Table should be created already in the Oracle Database.

        cur.execute("DELETE FROM Employee WHERE ID=:1",idd)

		
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

i=input("Enter ID of Employee to be deleted::")
database(i)

time.sleep(2)

print("\nSuccessfully Delete the Record\n\n")





    
