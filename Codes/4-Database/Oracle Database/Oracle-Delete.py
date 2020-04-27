
import cx_Oracle
import time

if__name__="__main__"

try:
    con = cx_Oracle.connect('arslanhaider/12345@AHS:1521/XE') 
    cur = con.cursor()

    #Table should be created already in the Database File.

    cur.execute(" DELETE FROM Employee WHERE ID='1' ")

		
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






    
