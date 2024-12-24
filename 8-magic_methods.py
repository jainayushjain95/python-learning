class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f'{self.title} by {self.author} in {self.pages} pages'

    def __len__(self):
        return self.pages

book = Book("Python Programming", "Ayush", 10)
print(book)
print(len(book))