#Database as a File
import sqlite3

if__name__="__main__"

try:
    con = sqlite3.connect('Pets.db') #only connection is changed for all types of databases,all other things remains same.

    
    cur = con.cursor() 

    #The First line ensures that if table already created then create table query ignored.

   #executescript is used to excute multiple quries.The following syntax should be followed.		
    cur.executescript("""DROP TABLE IF EXISTS Pets;  
		     CREATE TABLE Pets(Id INT, Name TEXT, Price INT);
		     INSERT INTO Pets VALUES(1, 'Cat', 400);
		     INSERT INTO Pets VALUES(2, 'Dog', 600);""")


  
    pets = ((3, 'Rabbit', 200),
	    (4, 'Bird', 60),
	    (5, 'Goat', 500))

    #executemany is used to excute multiple inserts into table.The following syntax should be followed.

    cur.executemany("INSERT INTO Pets VALUES(?, ?, ?)", pets)

		
    con.commit() #commit is used to make records(inserts) a part of database.

    cur.execute("SELECT * FROM Pets")  #Here we write the queries to fetch data from database.
    data = cur.fetchall()
		
    for row in data:
        print(row)

except sqlite3.Error:

    if con:
        con.rollback()

finally:
		
    if con:
        con.close()

    
