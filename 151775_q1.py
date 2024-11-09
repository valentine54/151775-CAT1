class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        self.is_borrowed = True

    def mark_as_returned(self):
        self.is_borrowed = False

class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            book.mark_as_borrowed()
            self.borrowed_books.append(book)
            print(f"{self.name} borrowed '{book.title}'")
        else:
            print(f"'{book.title}' has already been borrowed.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.mark_as_returned()
            self.borrowed_books.remove(book)
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"{self.name} has not borrowed '{book.title}'.")

    def list_borrowed_books(self):
        print(f"{self.name}'s borrowed books:")
        for book in self.borrowed_books:
            print(f"- {book.title}")

# Interactive code example
if __name__ == "__main__":
    book1 = Book("The cow jumped over the moon", "Jonathan Biden")
    member1 = LibraryMember("Beatrice", "B-001")
    member1.borrow_book(book1)
    member1.list_borrowed_books()
    member1.return_book(book1)
