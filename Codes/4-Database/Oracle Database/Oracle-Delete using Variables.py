
import cx_Oracle
import time

def database(idd):


    try:
        con = cx_Oracle.connect('arslanhaider/12345@AHS:1521/XE') 
        cur = con.cursor()

        #Table should be created already in the Oracle Database.

        cur.execute("DELETE FROM Employee WHERE ID=:1",idd)

		
        con.commit()

        cur.execute("SELECT * FROM Employee")
        data=cur.fetchall()

        for row in data:
            print(row)

        
    except cx_Oracle.Error:
    
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





    
