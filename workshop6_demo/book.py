class Book:
    def __init__(self, title, author, isbn, price, stock=0):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.price = price
        self.__stock = stock

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Price: ${self.price}"

    def add_stock(self, quantity):
        self.__stock += quantity # __stock = __stork + quantity
    
    def sell_book(self, quantity):
        if quantity <= self.__stock:
            self.__stock -= quantity
            return True
        else:
            return False
    
    def get_stock(self):
        return self.__stock

class EBook(Book):
    def __init__(self, title, author, isbn, price, file_format, stock=0):
        super().__init__(title, author, isbn, price, stock)
        self.file_format = file_format
    
    def display_info(self):
        return f"{super().display_info()}, File Format: {self.file_format}"