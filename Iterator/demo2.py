class Book:
    def __init__(self, name) -> None:
        self._name = name
    
    def get_name(self):
        return self._name

    
class BookShelf:
    def __init__(self, capacity) -> None:
        self._books = [None] * capacity
        self._last = 0

    def add_book(self, book):
        self._books[self._last] = book
        self._last += 1

    def get_length(self):
        return self._last
    
    def get_book_at(self, index):
        return self._books[index]

    def iterator(self):
        return BookShelfIterator(self)


class BookShelfIterator:
    def __init__(self, book_shelf) -> None:
        self._book_shelf = book_shelf
        self._index = 0
    
    def has_next(self):
        if self._index < self._book_shelf.get_length():
            return True
        return False
    
    def next(self):
        book = self._book_shelf.get_book_at(self._index)
        self._index += 1
        return book


if  __name__ == '__main__':
    book_shelf = BookShelf(4)
    book_shelf.add_book(Book('Apple'))
    book_shelf.add_book(Book('banana'))
    book_shelf.add_book(Book('cat'))
    book_shelf.add_book(Book('damn'))
    it = book_shelf.iterator()
    while it.has_next():
        print(it.next().get_name())