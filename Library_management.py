
from datetime import date

class Author:
    id_generator = 1

    def __init__(self, name, bio):
        self.id = Author.id_generator
        Author.id_generator += 1
        self.name = name
        self.bio = bio


class Book:
    id_generator = 1

    def __init__(self, title, author, isbn, available_copies):
        self.id = Book.id_generator
        Book.id_generator += 1
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies


class BorrowRecord:
    id_generator = 1

    def __init__(self, book, borrowed_by):
        self.id = BorrowRecord.id_generator
        BorrowRecord.id_generator += 1
        self.book = book
        self.borrowed_by = borrowed_by
        self.borrow_date = date.today()
        self.return_date = None



class LibraryService:
    def __init__(self):
        self.authors = []
        self.books = []
        self.borrow_records = []

    def list_authors(self):
        return self.authors

    def create_author(self, name, bio):
        author = Author(name, bio)
        self.authors.append(author)
        return author

    def create_book(self, title, author, isbn, available_copies):
        book = Book(title, author, isbn, available_copies)
        self.books.append(book)
        return book

    def list_books(self):
        return self.books

    def borrow_book(self, book_id, borrowed_by):
        book = next((b for b in self.books if b.id == book_id), None)
        if not book:
            raise Exception("Book not found")
        if book.available_copies <= 0:
            raise Exception("No copies available")

        book.available_copies -= 1
        record = BorrowRecord(book, borrowed_by)
        self.borrow_records.append(record)
        return record

    def return_book(self, record_id):
        record = next((r for r in self.borrow_records if r.id == record_id), None)
        if not record:
            raise Exception("Borrow record not found")

        record.return_date = date.today()
        record.book.available_copies += 1
        return record

    def generate_report(self):
        total_authors = len(self.authors)
        total_books = len(self.books)
        borrowed_books = sum(1 for r in self.borrow_records if not r.return_date)

        return {
            "total_authors": total_authors,
            "total_books": total_books,
            "borrowed_books": borrowed_books
        }



if __name__ == "__main__":
    service = LibraryService()

    
    author = service.create_author("J.K. Rowling", "British author")
    book = service.create_book("Harry Potter", author, "9780747532743", 10)

    try:
        record = service.borrow_book(book.id, "John Doe")
        print(f"Borrowed book: {record.book.title}")

        service.return_book(record.id)
        print(f"Returned book: {record.book.title}")
    except Exception as e:
        print(e)

    report = service.generate_report()
    print(f"Library Report: {report}")
