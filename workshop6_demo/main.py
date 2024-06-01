from book import Book, EBook

def main():
    book1 = Book("Harry Potter", "Nobody", "12345347", 10.99, 5)
    book2 = EBook("How to program in Python", "Capsen", "234234234", 20, "pdf", 10)

    print(book1.get_stock())
    print(book2.display_info())
    book1.title = "Three kingdom"
    if(book1.sell_book(3)):
        print(f"after sold 3 {book1.title}, we have {book1.get_stock()} left")

if __name__ == "__main__":
    main()