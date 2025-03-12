import mysql.connector
import random
conn = mysql.connector.connect(host = "localhost" , user = "root" , password = "admin@123",database = "Bank")
cursor = conn.cursor()
class Bank:
    def deposite(self):
        acc = int(input("Enter Account Number for Deposite : "))
        amount = int(input("Enter Amount to Deposite: "))
        if amount < 0:
            return print("Amount should be greater than 0...")
        query = "select * from customer where acc_no = %s"
        args=(acc,)
        cursor.execute(query,args)
        res = cursor.fetchone()
        if res:
            uquery = "UPDATE customer SET balance = balance + %s WHERE acc_no = %s"
            args=(amount,acc)
            cursor.execute(uquery,args)
            conn.commit()
            print("Money Deposited Successfully....")
            print("Here is you updated Balance : ")
            query = "select * from customer where acc_no = %s"
            args=(acc,)
            cursor.execute(query,args)
            res = cursor.fetchone()
            print(res)
        else:
            print("user doesnt exists with this account number..")

    def withdrawal(self):
        acc = int(input("Enter Account Number for  withdrawal : "))
        
        query = "select * from customer where acc_no = %s"
        args=(acc,)
        cursor.execute(query,args)
        res = cursor.fetchone()
        if res:
            amount = int(input("Enter Amount to withdrawal: "))
            if amount < 0:
                return print("Amount should be greater than 0...")
            if amount > res[2]:
                print("Insufficent balance !!!")
                return
            uquery = "UPDATE customer SET balance = balance - %s WHERE acc_no = %s"
            args=(amount,acc)
            cursor.execute(uquery,args)
            conn.commit()
            print("Money Withdrawal Successfully....")
            print("Here is you updated Balance : ")
            query = "select * from customer where acc_no = %s"
            args=(acc,)
            cursor.execute(query,args)
            res = cursor.fetchone()
            print(res)
        else:
            print("user doesnt exists with this account number..")

    def check_balance(self):
        acc = int(input("Enter Your Account Number  : "))
        query = "select * from customer where acc_no = %s"
        args=(acc,)
        cursor.execute(query,args)
        res = cursor.fetchone()
        if res:
            print("Your Name : ",res[1])
            print("Your Account Balance : ",res[2])
        else:
            print("user doesnt exists with this account number..")
class Customer:
    def __init__(self):
        self.acc_no = 0
        self.name = ""
        self.balance = 0.00
    def add_user(self):
        self.name = str(input("Enter Your name : "))
        self.balance = float(input("Enter Initail deposite amount: "))
        self.acc_no = float(random.randint(100,999))
        query = f"insert into customer(acc_no,name,balance)values('{self.acc_no}','{self.name}','{self.balance}');"
        cursor.execute(query)
        conn.commit()
        print("Customer Added Successfully...")
    def show_users(self):
        di = {}
        lst=[]
        query = "select * from customer"
        cursor.execute(query)
        res = cursor.fetchall()
        # print(res[1])
        for data in res:
            print(data[0],data[1],data[2])
cust = Customer()
b = Bank()

while True:
    print("|---------------Menu------------|")
    print(" 1. Add Customer \n 2. Show Customer .\n 3.Deposite . \n 4.Withdrawl .\n 5.Check Balance .\n 6.Exit\n")
    ch = int(input("Enter Your Choice : "))
    if ch == 1:
        cust.add_user()
    elif ch == 2:
        cust.show_users()
    elif ch == 3 :
        b.deposite()
    elif ch == 4 :
        b.withdrawal()
    elif ch == 5 :
        b.check_balance()
    elif ch == 6 :
        print("Good Bye...")
        break
    else:
        print("Invalid Choice")

# b.withdrawal()
# b.check_balance()
# b.deposite()
# cust.add_user()
# cust.show_users()