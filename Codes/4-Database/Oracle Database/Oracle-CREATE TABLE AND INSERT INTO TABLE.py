
import cx_Oracle 

if__name__="__main__"

try:
    #con=cx_Oracle.connect('username/password@host:port/SID')  #Syntax for Oracle database connection.
    con = cx_Oracle.connect('arslanhaider/12345@AHS:1521/XE') 

    
    cur = con.cursor() 

    #The First line ensures that if table already created then create table query ignored.

   #executestring is used to excute multiple quries.The following syntax should be followed.		
    cur.execute("CREATE TABLE Password(Username varchar(255),Password INT)")
    cur.execute("INSERT INTO Password VALUES('arslanhaider',12345)")
    cur.execute("INSERT INTO Password VALUES('arslanhaider95',123456)")
    cur.execute("INSERT INTO Password VALUES('arslanhaider143',123457)")
    cur.execute("INSERT INTO Password VALUES('arslanhaider123',123458)")

		
    con.commit() #commit is used to make records(inserts) a part of database.

    cur.execute("SELECT * FROM Password")  #Here we write the queries to fetch data from database.
    data = cur.fetchall()
		
    for row in data:
        print(row)

except cx_Oracle.Error:

    if con:
        con.rollback()

finally:
		
    if con:
        con.close()

    
