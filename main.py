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
    pass
        
book1 = Book('Xusanboy Tursunov', 2023, 'U bu siz emas', 1)

print(book1.getInfo())