class Calculator:
    def addition(self):
        try:
            a = int(input("Enter First Number : "))
            b = int(input("Enter Second Number : "))
            print(f"Addition of {a} and {b} is : {a+b}")
        except ValueError:
            print("Enter Valid Number")
    def subtraction(self):
        try:
            a = int(input("Enter First Number : "))
            b = int(input("Enter Second Number : "))
            print(f"Subtraction of {a} and {b} is : {a-b}")
        except ValueError:
            print("Enter Valid Number")

    def multiplication(self):
        try:
            a = int(input("Enter First Number : "))
            b = int(input("Enter Second Number : "))    
            print(f"Multiplication of {a} and {b} is : {a*b}")
        except ValueError:
            print("Enter Valid Number")
    def divison(self):
        try:
            a = int(input("Enter First Number : "))
            b = int(input("Enter Second Number : "))
            print(f"Divison of {a} and {b} is : {a/b}")
        except ValueError:
            print("Enter Valid Number")
        except ZeroDivisionError:
            print("Can not divide by zero")        
cal = Calculator()



while True:
    print("|--------Calculator-------|")
    print("1.Addition \n2. Subtraction \n3.Multiplication \n4.Divison \n5.Exit")
    print("Enter Your Choice : ")
    ch = int(input())
    if ch == 1:
        cal.addition()
        
    elif ch == 2:
        cal.subtraction()
        
    elif ch == 3:
        cal.multiplication()

    elif ch == 4:
        cal.divison()
        
    elif ch == 5:
        break
    else:
        print("Enter Valid Choice")