class Book:
    def __init__(self, author, year, name, isbn) -> None:
        self.author = author
        self.year = year
        self.name = name
        self.isb = isbn
    def getAuthor(self) -> str:
        return self.author
    def getYear(self) -> int:
        return self.year
    def getName(self) -> str:
        return self.name
    def getIsb(self) -> int:
        return self.isb
    def getInfo(self) -> str:
        return f'Author: {self.getAuthor()}\nYear: {self.getYear()}\nName: {self.getName()}\nIsb: {self.getIsb()}'

class Library:

    def __init__(self) -> None:
        self.books = []

    def addBook(self, book):
        self.books.append(book)

    def removeBook(self, book):
        self.books.remove(book)
    
    def show(self):
        return self.books
        
book1 = Book('Author1', 2023, 'Name1', 1)
book2 = Book('Author2', 2022, 'Name2', 2)
book3 = Book('Author3', 2021, 'Name3', 3)

library = Library()

library.addBook(book1)
library.addBook(book2)
library.addBook(book3)

for book in library.show():
    print(book.getInfo())