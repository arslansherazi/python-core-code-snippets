import psycopg2
import time

def database(idd):

    try:
        conn = psycopg2.connect(database="MHS", user="postgres", password="ars123", host="localhost", port="5432")
        cur = conn.cursor()

        #Table should be created already in the Postgres Database.

        cur.execute("DELETE FROM Employee WHERE ID=%s",(idd,))  #If we use single variable then put bracket around it and put comma after it.It is necessary.

		
        conn.commit()

        cur.execute("SELECT * FROM Employee")
        data=cur.fetchall()

        for row in data:
            print(row)

        
    except psycopg2.Error:
    
        if conn:
            conn.rollback()

    finally:
		
        if conn:
            conn.close()

if__name__="__main__"

i=input("Enter ID of Employee to be deleted::")
database(i)

time.sleep(2)

print("\nSuccessfully Delete the Record\n\n")





    
