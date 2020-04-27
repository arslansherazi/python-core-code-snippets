#Database as a File
import psycopg2

if__name__="__main__"

try:
    #specified Database (Company in this programme) should be created already
    #Employee should be according to the user(postgres).It can be changes(according to our choice)
    conn = psycopg2.connect(database="MHS", user="postgres", password="ars123", host="127.0.0.1", port="5432")
    
    cur=conn.cursor()
   
    #The Following Query Create Table "Employee"(We can change name according to our choice)
    #If we run this programme more than 1 time then following query does not create same table again and again because it already exists.but same Inserts are possible
    cur.execute("CREATE TABLE IF NOT EXISTS Employee(ID varchar(255),Name varchar(255),Contact bigint)")

    #Different Data types of attributes can be seen from "http://www.tutorialspoint.com/postgresql/postgresql_data_types.htm" and also from internet.
    #Appropriate data type should be define for attribute according to its type and size.Other wise data doesnt insert into the table.
    
    
    #The Following Queries inserts data into the table "Employee"
    cur.execute("INSERT INTO Employee VALUES('MHS12','Arslan Haider',03336664142)")
    cur.execute("INSERT INTO Employee VALUES('MHS13','Fasi Haider',03034299655)")
    cur.execute("INSERT INTO Employee VALUES('MHS14','Waqar Haider',03006176437)")
    cur.execute("INSERT INTO Employee VALUES('MHS15','Ghulam Haider',03041997272)")
    cur.execute("INSERT INTO Employee VALUES('MHS16','Husnain Shah',03013130189)")


    conn.commit()#Queries should be committed to make them permanent part of Database
   

    #The Following Query Selects all data from the Table "Employee"
    cur.execute("SELECT * FROM Employee")
    data=cur.fetchall()
    #fetchall() function is used to fetch all rows from the Table at a time.
    #fetchone() function is used to fetch one row at a time from Table.

    for row in data:
        print(row)

except psycopg2.Error:
    if(conn):
        conn.rollback()
finally:
    if(conn):
        conn.close()
    
