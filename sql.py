import sqlite3 

# Connect to sqlite 
connection = sqlite3.connect("student.db")

cursor = connection.cursor()

# Create a table 
table_info = """
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25), SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

# Insert records 
cursor.execute("INSERT INTO STUDENT VALUES('John Doe', '10th Grade', 'A', 85);")
cursor.execute("INSERT INTO STUDENT VALUES('Jane Smith', '10th Grade', 'B', 92);")
cursor.execute("INSERT INTO STUDENT VALUES('Emily Davis', '9th Grade', 'A', 78);")
cursor.execute("INSERT INTO STUDENT VALUES('Michael Brown', '9th Grade', 'C', 88);")
cursor.execute("INSERT INTO STUDENT VALUES('Sarah Wilson', '10th Grade', 'A', 95);")

# Display all the records 
print("The inserted records are:")

data = cursor.execute("SELECT * FROM STUDENT;")
for row in data:
    print(row)

# Close the connection
connection.commit()
connection.close() 
