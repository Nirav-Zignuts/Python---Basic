import mysql.connector

conn = mysql.connector.connect(host = "localhost" , user = "root" , password = "admin@123",database = "first")
cursor = conn.cursor()
print("|--------Data-------|")
query = "select * from category"
cursor.execute(query)
res = cursor.fetchall()
for data in res:
    print(data)