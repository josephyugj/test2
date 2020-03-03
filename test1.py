import pymssql

conn = pymssql.connect(server="163.13.43.178",user="tku",password="tkuiosh", database="course")

cursor = conn.cursor()

cursor.execute("select * from rating0719")

row = cursor.fetchone()

while row:
    print(row)
    row = cursor.fetchone()

db.close()

