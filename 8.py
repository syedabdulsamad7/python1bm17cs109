import sqlite3
conn=sqlite3.connect("f1.db")
cur=conn.cursor()
conn.execute("CREATE TABLE STUDENT(ID INTEGER PRIMARY KEY,Name TEXT,Age INTEGER)")
print("table created..")
conn.execute("INSERT INTO STUDENT(ID,Name,Age) VALUES(12,'AAAAAA',12)")
conn.execute("INSERT INTO STUDENT(ID,Name,Age) VALUES(15,'BBBBBB',12)")
conn.execute("INSERT INTO STUDENT(ID,Name,Age) VALUES(13,'CCCCCC',13)")
conn.execute("INSERT INTO STUDENT(ID,Name,Age) VALUES(18,'DDDDDD',16)")
conn.execute("INSERT INTO STUDENT(ID,Name,Age) VALUES(22,'EEEEEE',15)")
print("Values inserted.........")
print()
print("Student table:")
cur=conn.execute("SELECT * FROM STUDENT")
print("----------------------------------------------------------")
print("student id".ljust(10),"Name".ljust(10),"age".ljust(10))
print("----------------------------------------------------------")

for row in cur:
    print(str(row[0]).ljust(10),row[1].ljust(10),str(row[2]).ljust(10))

print()
print("student details whose age>12")

cur=conn.execute("SELECT ID,Name,Age FROM STUDENT WHERE Age>12")
print("----------------------------------------------------------")
print("student id".ljust(10),"Name".ljust(10),"age".ljust(10))
print("----------------------------------------------------------")

for row in cur:
    print(str(row[0]).ljust(10),row[1].ljust(10),str(row[2]).ljust(10))

conn.execute("UPDATE STUDENT SET ID=? WHERE AGE=?",(20,13))
cur=conn.execute("SELECT * FROM STUDENT")
print()
print("after updating the student id to 20 whose age=13")
print("----------------------------------------------------------")
print("student id".ljust(10),"Name".ljust(10),"age".ljust(10))
print("----------------------------------------------------------")

for row in cur:
    print(str(row[0]).ljust(10),row[1].ljust(10),str(row[2]).ljust(10))

conn.execute("DELETE FROM STUDENT WHERE Name='EEEEEE'")
cur=conn.execute("SELECT * FROM STUDENT")
print()
print("after deleting student EEEEEE..")
print("----------------------------------------------------------")
print("student id".ljust(10),"Name".ljust(10),"age".ljust(10))
print("----------------------------------------------------------")

for row in cur:
    print(str(row[0]).ljust(10),row[1].ljust(10),str(row[2]).ljust(10))
conn.commit()
conn.close()
