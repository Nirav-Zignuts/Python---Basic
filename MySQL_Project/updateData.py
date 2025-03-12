import mysql.connector

conn = mysql.connector.connect(host = "localhost" , user = "root" , password = "admin@123",database = "first")
cursor = conn.cursor()
cid = int(input("Enter id whose data you want to update : "))
cname = str(input("enter name : "))
query = "UPDATE category SET name = %s where id = %s"
args = (cname,cid)
cursor.execute(query,args)
conn.commit()
print(" here is your updated data : ")
query= f"select * from category where id = {cid}"
cursor.execute(query)
res = cursor.fetchall()
for data in res:
    print(data)