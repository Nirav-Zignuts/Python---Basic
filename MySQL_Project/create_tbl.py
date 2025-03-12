import mysql.connector

conn = mysql.connector.connect(host = "localhost" , user = "root" , password = "admin@123",database = "first")
cursor = conn.cursor()
query ="CREATE TABLE Category( id int(5) PRIMARY KEY , name varchar(20) NOT NULL UNIQUE, description varchar(100) NOT NULL)"
query_prduct = "create table product( id int(5) primary key , name varchar(50) not null unique , description varchar(100) not null , category_id int(5) not null , foreign key(category_id) references Category(id) on delete cascade)"
cursor.execute(query)
cursor.execute(query_prduct)
print("tables created successfully:")
