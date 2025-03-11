class Book:
    def __init__(self):
        self.books = {}
    def add_book(self):
        lst = []
        print("Enter Book Details :")
        title = str(input("Enter Title of the Book : ")).lower()
        lst.append(str(input("Enter Book authore name : ")))
        lst.append(int(input("Enter Book price : ")))
        self.books[title] = lst
        print("Book Details Stored Successfully")
        
    def remove_book(self):
        name = str(input("Enter  name(Title) of Book to remove: ")).lower()
        b = self.books.get(name)
        if b is not None:
            del self.books[name]
        else:
            print(f"{name} is not exists please enter again !!!.")

    def search_book(self):
        name = str(input("Enter  name(Title) of Book you want : ")).lower()
        b = self.books.get(name)
        if b is not None:
            print(f"Book Details : \nTitle : {name}\nAuthor : {b[0]}\nPrice : {b[1]}")
        else:
            print(f"requeted book ({name}) doesn`t exists...")
bok = Book()

while True:
    print("|--------LMS-------|")
    print("1.Add Book\n2.Remove Book\n3.Search book\n4.Exit")
    print("Enter Your Choice : ")
    ch = int(input())
    if ch == 1:
        bok.add_book()
        
    elif ch == 2:
        bok.remove_book()
        
    elif ch == 3:
        bok.search_book()
        
    elif ch == 4:
        break
    else:
        print("Enter Valid Choice")
