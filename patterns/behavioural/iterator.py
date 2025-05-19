
class BookIterator:
    """Iterator for the Book collection."""

    def __init__(self, books):
        self.books = books
        self.index = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < len(self.books):
            book = self.books[self.index]
            self.index += 1
            return book
        else:
            raise StopIteration
        

class BookCollection:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def __iter__(self):
        return BookIterator(self._books)
    

if __name__ == "__main__":
    collection = BookCollection()
    collection.add_book("The Great Gatsby")
    collection.add_book("1984")
    collection.add_book("To Kill a Mockingbird")
    collection.add_book("Pride and Prejudice")
    collection.add_book("The Catcher in the Rye")

    for book in collection:
        print(book)