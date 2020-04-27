
import cx_Oracle
import time

if__name__="__main__"

try:
    con = cx_Oracle.connect('arslanhaider/12345@AHS:1521/XE') 
    cur = con.cursor()

    #Table should be created already in the Oracle Database.

    cur.execute("UPDATE Employee  SET ID='Sherazi192'   WHERE Name='Sherazi'")

		
    con.commit()

except cx_Oracle.Error:

    if con:
        con.rollback()

finally:
		
    if con:
        con.close()






    
