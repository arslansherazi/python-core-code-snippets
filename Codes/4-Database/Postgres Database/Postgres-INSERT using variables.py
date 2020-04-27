
import psycopg2
import time

def Database(name,idd,contact):

    try:
        con = psycopg2.connect(database="MHS", user="postgres", password="ars123", host="localhost", port="5432") 

        
    
        cur = con.cursor()

        #This query checks that whether the table already exist in the database.
        #if so then it does not create new table.and if table exists then it creates the table.It means that table is created just once then
        #all the entries are gone to the same table.
          
        cur.execute("CREATE TABLE IF NOT EXISTS Employee(ID varchar(255),Name varchar(255),Contact INT)")

        cur.execute("INSERT INTO Employee VALUES(%s,%s,%s)",(idd,name,contact))

		
        con.commit()
        cur.execute("SELECT * FROM Employee")
        data = cur.fetchall()
		
        for row in data:
            print(row)

    except psycopg2.Error:

        if con:
            con.rollback()

    finally:
		
        if con:
            con.close()

if__name__="__main__"

while True:
    n=input("Enter Name::")
    i=input("Enter Idd::")
    c=input("Enter Contact No::")
    print("\n\nRecord Successfully Stored......\n\n")
    Database(n,i,c)
    print("\n\n")

    time.sleep(3)

    


    
