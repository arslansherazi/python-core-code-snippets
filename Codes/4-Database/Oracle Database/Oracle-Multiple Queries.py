
import cx_Oracle

if__name__="__main__"

try:
    con = cx_Oracle.connect('arslanhaider/12345@AHS:1521/XE') #only connection is changed for all types of databases,all other things remains same.

    
    cur = con.cursor() 

   #Table Should be created already in the database
  
    pets = [(3, 'Rabbit', 200),
	    (4, 'Bird', 60),
	    (5, 'Goat', 500)]

    #executemany is used to excute multiple inserts into table.The following syntax should be followed.

    cur.executemany("INSERT INTO Animal VALUES(:1, :2, :3)", (pets))

		
    con.commit() #commit is used to make records(inserts) a part of database.

   

except cx_Oracle.Error:

    if con:
        con.rollback()

finally:
		
    if con:
        con.close()

    
