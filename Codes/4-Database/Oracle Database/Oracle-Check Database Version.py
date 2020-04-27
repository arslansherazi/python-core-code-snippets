
import cx_Oracle

if__name__="__main__"

try:

    conn=cx_Oracle.connect('arslanhaider/12345@AHS:1521/XE')

    print(conn.version)

except cx_Oracle.Error:
    if(conn):
        conn.rollback()
finally:
    if(conn):
        conn.close()
    
