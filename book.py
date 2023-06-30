class Book:

    def __init__(self, Title, Author, Publishing_date, Price):
        self.Title = Title
        self.Author = Author
        self.Publishing_date = Publishing_date
        self.Price = Price

    def view(self):
        return "Book Title: " + self.Title, "Book Author: " + self.Author, "Book release: " + self.Publishing_date, "Book Price: " + self.Price


MyBook = Book("Seras-tu là ", "Guilaume Musso", "04 Mai 2006", "9€")
print(MyBook.view())
