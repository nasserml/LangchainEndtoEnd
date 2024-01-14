import sqlite3

# connect to sqlite
connection = sqlite3.connect("student.db")

# create a cursor
cursor = connection.cursor()

# create a table
table_info = """ 
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""

cursor.execute(table_info)

# insert records
cursor.execute('''Insert Into STUDENT values('Nasser','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Ahmed','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('may','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('mahmoud','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('mohamed','DEVOPS','A',35)''')

# display all the records
print("thje inserted records are ")
data = cursor.execute("Select * from STUDENT")

for row in data:
    print(row)

## close the connection 
connection.commit()
connection.close()