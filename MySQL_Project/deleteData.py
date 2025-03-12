import mysql.connector

conn = mysql.connector.connect(host = "localhost" , user = "root" , password = "admin@123",database = "first")
cursor = conn.cursor()
cid = int(input("Enter id whose reocord you want to delete: "))
query = "DELETE FROM category WHERE id = %s"
args = (cid,)
cursor.execute(query,args)
conn.commit()
print("Record Deleted Successfully ",cursor.rowcount," rows affected ")