from mysql.connector import connect, Error

try:
    connection = connect(
        host="localhost",
        user="root",
        password="admin@123",
    )  
    print(connection)
except Error as e:
    print(e)

#print("Connected Successfully:")
cursor = connection.cursor()
db_name = str(input("Enter Database Name You want to create : "))

cursor.execute("show databases")
dbs = [db[0] for db in cursor.fetchall()]

try:
    if db_name not in dbs:
            cursor.execute(f"CREATE DATABASE {db_name}")
            print(f"Dtabase {db_name} created successfully.")
except Error as e:
    print(f"Database with name {db_name} already exists !!!")
     