
import psycopg2
import time

if__name__="__main__"

try:
    con = psycopg2.connect(database="MHS", user="postgres", password="ars123", host="localhost", port="5432") 
    cur = con.cursor()

    #Table should be created already in the Database File.

    cur.execute("UPDATE Employee SET Name='Arslan Haider Sherazi'   WHERE ID='MHS13'")

		
    con.commit()

    cur.execute("SELECT * FROM Employee")
    data=cur.fetchall()

    for row in data:
        print(row)

except psycopg2.Error:

    if con:
        con.rollback()

finally:
		
    if con:
        con.close()






    
