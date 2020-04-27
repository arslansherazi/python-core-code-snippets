#Database as a File
import sqlite3 as sql

if__name__="__main__"

try:

    #This code does not execute on second run because the table is already in database and new table with same name does not create.
    #For Solution See the Next code which is Multiple Queries.

    conn=sql.connect('DBfile.db') #only connection is changed for all types of databases,all other things remains same.
    cur=conn.cursor()
    cur.execute("CREATE TABLE Password(Username varchar(255),Password INT)")
    cur.execute("INSERT INTO Password VALUES('arslanhaider',12345)")
    cur.execute("INSERT INTO Password VALUES('arslanhaider95',123456)")
    cur.execute("INSERT INTO Password VALUES('arslanhaider143',123457)")
    cur.execute("INSERT INTO Password VALUES('arslanhaider123',123458)")
	
    #cur.execute("SELECT Username FROM Password WHERE Password=123456")
    cur.execute("SELECT * FROM Password)
    data=cur.fetchall()

    for row in data:
        print(row)

except sql.Error:
    if(conn):
        conn.rollback()
finally:
    if(conn):
        conn.close()
    
