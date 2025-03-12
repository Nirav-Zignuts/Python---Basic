import mysql.connector

conn = mysql.connector.connect(host = "localhost" , user = "root" , password = "admin@123",database = "first")
cursor = conn.cursor()
cnt = int(input("how many recordes you want to insert : "))
for i in range(cnt):
    name = str(input("Enter Name : "))
    description = str(input("Enter Description : "))
    query = f"insert into Category(id , name , description) values('{i+1}','{name}' , '{description}')"
    cursor.execute(query)  
    conn.commit()
print("data added successfully")