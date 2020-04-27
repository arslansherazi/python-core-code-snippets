
import cx_Oracle
import time

def Database(name,idd,contact):

    try:
        con = cx_Oracle.connect('arslanhaider/12345@AHS:1521/XE') 

        
    
        cur = con.cursor()

        #Table should be created already in the Oracle Database.

        cur.execute("INSERT INTO Employee VALUES(:1, :2, :3)",( name,idd,contact))

		
        con.commit()
        cur.execute("SELECT * FROM Employee")
        data = cur.fetchall()
		
        for row in data:
            print(row)

    except cx_Oracle.Error:

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
    Database(n,i,c)

    time.sleep(3)

    print("Record Successfully Stored......\n\n")


    
