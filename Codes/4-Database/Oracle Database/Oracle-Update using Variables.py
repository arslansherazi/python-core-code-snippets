
import cx_Oracle
import time

def database(idd,name):


    try:
        con = cx_Oracle.connect('arslanhaider/12345@AHS:1521/XE') 
        cur = con.cursor()

        #Table should be created already in the Oracle Database.

        cur.execute("UPDATE Employee  SET ID=:1   WHERE Name=:2",(idd,name))

		
        con.commit()

    except cx_Oracle.Error:
    
        if con:
            con.rollback()

    finally:
		
        if con:
            con.close()

if__name__="__main__"

i=input("Enter Id to be changed::")
n=input("Enter Name for which Id to be changed::")
database(i,n)

time.sleep(2)

print("\nSuccessfully change the ID\n\n")





    
