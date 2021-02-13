# Create a library class
# display book
# lend book - (who owns the book if not present)
# add book
# return book
# HarryLibrary = Library(listofbooks, library_name)
#dictionary (books-nameofperson)
# create a main function and run an infinite while loop asking
# users for their input

class library():
    #constuctur for creating the library
    def __init__(self,listofbooks,library_name):
        self.books=listofbooks
        self.name=library_name

    #display the books which are in Library
    def display_book(self):
        print(f"{self.name}={self.books}")
        print("the library is displayed successfuly")

    #adding the book to the library
    def add_book(self,book):
        self.books.append(book)
        print("the book is added successfuly")

    #delete the book to the library
    def delete_book(self,book):
        if book in self.books:
            self.books.remove(book)
            print("the book is deleted successfuly")
        else:print("enter the available book in library")

    #lending the book to the person
    dictionary={}
    def lend_book(self,name,book):
        if book in self.books:
            self.dictionary[book]=name
            self.books.remove(book)
            print("the book is lent successfuly")
        elif book in self.dictionary:
            print(f"the book is lend to [{self.dictionary[book]}] plesase take any other book")
        else: print("please enter book name properly")

    #returning the book to library
    def return_book(self,book):
        if book in self.dictionary:
            del self.dictionary[book]
            self.books.append(book)
            print("the book is returned successfuly")
        else: print("the book was never lend or the book was not in the librarly")

#creating library and assining a name
nameofthelibrary=input("enter the library name...: ")
nameofthelibrary=library(["vinna","ranna","monica","nayana"],nameofthelibrary)

while True:
    if __name__ == "__main__":
        print("1. Display books")
        print("2. Add book")
        print("3. delete book")
        print("4. Lend book")
        print("5. Return book")
        print("exit - to exit the menu")
        choice=input("enter the option you need from the list:")
        if choice=="1":
            nameofthelibrary.display_book()
        elif choice=="2":
            book=input("enter the book name:")
            nameofthelibrary.add_book(book)
        elif choice=="3":
            book=input("enter the book name:")
            nameofthelibrary.delete_book(book)
        elif choice=="4":
            nameofthelibrary.display_book()
            name=input("enter the person name:")
            book=input("enter the book name:")
            nameofthelibrary.lend_book(name,book)
        elif choice=="5":
            book=input("enter the book name:")
            nameofthelibrary.return_book(book)
        elif choice=="exit":
            exit()
        else:print("you have entered wrong option")
    print("\n")