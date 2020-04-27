#Database as a File
import sqlite3 as sql

if__name__="__main__"

try:

    conn=sql.connect('DBfile.db') #only connection is changed for all types of databases,all other things remains same.

    cur=conn.cursor()
    cur.execute('SELECT SQLITE_VERSION()')

    data=cur.fetchone()

    print("SQLITE VERSION="+str(data))

except sqlite3.Error,e:
    if(conn):
        conn.rollback()
finally:
    if(conn):
        conn.close()
    
