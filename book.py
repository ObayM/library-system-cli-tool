import datetime
from rich.console import Console
from rich.table import Table

console = Console()

class Book:

    def __init__(self, book_id, name, field, num_papers, writer, publisher, publish_year, borrow_price, is_borrowed=False, rate=0):
        self.id = book_id
        self.name = name
        self.field = field
        self.num_papers = num_papers
        self.writer = writer
        self.publisher = publisher
        self.publish_year = publish_year
        self.is_borrowed = is_borrowed
        self.borrow_price = borrow_price
        self.rate = rate
        self.reviews = []

    def update_info(self, key, value):

        if hasattr(self, key):

            try:
                attr_type = type(getattr(self, key))
                setattr(self, key, attr_type(value))
                console.print(f"[bold green]Successfully updated '{key}' to '{value}'.[/bold green]")
            except ValueError:
                console.print(f"[bold red]Error: Invalid value type for '{key}'.[/bold red]")
        else:
            console.print(f"[bold red]Error: '{key}' is not a valid field.[/bold red]")

    def show_all_info(self):

        table = Table(title=f"[bold cyan]Book Details: {self.name}[/bold cyan]", show_header=True, header_style="bold magenta")
        table.add_column("Attribute", style="dim", width=20)
        table.add_column("Value")

        info = {
            "ID": self.id,
            "Name": self.name,
            "Field": self.field,
            "Number of Papers": str(self.num_papers),
            "Writer": self.writer,
            "Publisher": self.publisher,
            "Publish Year": str(self.publish_year),
            "Age (Years)": str(self.calculate_age()),
            "Borrowed Status": "Yes" if self.is_borrowed else "No",
            "Borrow Price": f"${self.borrow_price:.2f}",
            "Rating": f"{self.rate}/5 Stars"
        }

        for key, value in info.items():
            table.add_row(key, value)

        console.print(table)


    def calculate_age(self):

        current_year = datetime.datetime.now().year
        return current_year - self.publish_year


    def add_review(self, review_text, review_type):

        if review_type.lower() not in ['good', 'bad']:
            console.print("[bold red]Invalid review type. Please use 'good' or 'bad'.[/bold red]")
            return
        self.reviews.append({"text": review_text, "type": review_type})
        console.print("[bold green]Review added successfully.[/bold green]")


    def show_reviews(self):

        console.print(f"\n--- Reviews for [bold cyan]{self.name}[/bold cyan] ---")
        if not self.reviews:
            console.print("[yellow]No reviews for this book yet.[/yellow]")
        else:
            for review in self.reviews:
                color = "green" if review['type'].lower() == 'good' else "red"
                console.print(f"- \"{review['text']}\" ([{color}]{review['type']}[/{color}])")