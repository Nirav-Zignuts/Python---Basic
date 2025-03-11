# catch_first_only.py

"""exceptions = [FileNotFoundError(),ZeroDivisionError(),  NameError()]
num_zd_errors = num_fnf_errors = num_name_errors = 0

try:
    for e in exceptions:
        raise e
except ZeroDivisionError:
    num_zd_errors += 1
except FileNotFoundError:
    num_fnf_errors += 1
except NameError:
    num_name_errors += 1
finally:
    print(f"ZeroDivisionError was raised {num_zd_errors} times.")
    print(f"FileNotFoundError was raised {num_fnf_errors} times.")
#     print(f"NameError was raised {num_name_errors} times.")"""
# class MyException(Exception):
#     def __init__(self,message,error_code):
#         super().__init__(message)
#         self.error_code = error_code
        
#     def __str__(self):
#         return f"{self.args[0]} (error code : {self.error_code})"
        
# def div(a,b):
#     if b == 0:
#         raise MyException("A number cant be divide by zero",400)
#     return a/b
        
  
# try:
#     print(div(10,0))
# except MyException as e:
#     print(e)
# def method_decorator(func):
#     def wrapper(self, *args ):
#         print("Before method execution")
#         res = func(self, *args)
#         print("After method execution")
#         return res
#     return wrapper

# class MyClass:
#     @method_decorator
#     def say_hello(self,n):
#         print("Hello!",n)

# obj = MyClass()
# obj.say_hello(10)


with open("test.txt","w") as f:
    for i in range(10):
        f.write(str(i)+"\n")
with open("test.txt","r") as f:
    for line in f:
        print(line)
print("you wanna add some stuff to file or not")
data = str(input("Enter : "))
with open("test.txt","a") as f:
    f.write(data)   
with open("test.txt","r") as f:
    for line in f:
        print(line)