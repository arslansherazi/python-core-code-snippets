
import psycopg2
import time

def database(name,idd):
    
    try:
        con = psycopg2.connect(database="MHS", user="postgres", password="ars123", host="localhost", port="5432") 
        cur = con.cursor()

        #Table should be create already in the Oracle Database.

        cur.execute("UPDATE Employee  SET Name=%s   WHERE ID=%s",(name,idd))

		
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
            

if__name__="__main__"

n=input("Enter Name to be changed::")
i=input("Enter ID for which Name to be changed::")
database(n,i)

time.sleep(2)

print("\nSuccessfully change the ID\n\n")





    
