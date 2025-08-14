from book import Book, console

class Library:

    def __init__(self):

        self.library_db = {}

    def add_book(self):

        console.print("\n[bold yellow]--- Enter New Book Details ---[/bold yellow]")
        book_id = input("Enter book ID: ")

        if book_id in self.library_db:
            console.print("[bold red]Error: A book with this ID already exists.[/bold red]")
            return

        name = input("Enter book name: ")
        field = input("Enter book field: ")
        try:
            num_papers = int(input("Enter number of pages: "))
            publish_year = int(input("Enter publish year: "))
            borrow_price = float(input("Enter borrow price: "))
        except ValueError:
            console.print("[bold red]Invalid number entered. Please start over.[/bold red]")
            return

        writer = input("Enter writer name: ")
        publisher = input("Enter publisher name: ")

        new_book = Book(book_id, name, field, num_papers, writer, publisher, publish_year, borrow_price)
        self.library_db[book_id] = new_book
        console.print(f"\n[bold green]Success![/bold green] Book '[cyan]{name}[/cyan]' has been added to the library.")

    def find_book(self, book_id):

        return self.library_db.get(book_id)