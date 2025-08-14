from library import Library
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
import time

console = Console()

def interface():

    library = Library()
    
    console.print(Panel("[bold magenta]Welcome to the library management system! [/bold magenta]", border_style="green"))
    time.sleep(1)

    while True:
        console.print(Panel("""[bold cyan]
        1. Add New Book
        2. Search for a Book
        3. Show Book Reviews
        4. Add a Review for a Book
        5. Update Book Info
        6. Exit
        [/bold cyan]""", title="[bold]Main Menu[/bold]", border_style="blue"))

        choice = Prompt.ask("[bold]Enter your choice[/bold]", choices=["1", "2", "3", "4", "5", "6"], default="6")

        if choice == '1':
            library.add_book()

        elif choice == '2':
            book_id = Prompt.ask("Enter the book ID to search for")
            book = library.find_book(book_id)
            if book:
                book.show_all_info()
            else:
                console.print("[bold red]Error: Book not found.[/bold red]")

        elif choice == '3':
            book_id = Prompt.ask("Enter the book ID to see its reviews")
            book = library.find_book(book_id)
            if book:
                book.show_reviews()
            else:
                console.print("[bold red]Error: Book not found.[/bold red]")

        elif choice == '4':
            book_id = Prompt.ask("Enter the book ID to add a review for")
            book = library.find_book(book_id)
            if book:
                review_text = Prompt.ask("Enter your review")
                review_type = Prompt.ask("Enter review type", choices=["good", "bad"], default="good")
                book.add_review(review_text, review_type)
            else:
                console.print("[bold red]Error: Book not found.[/bold red]")

        elif choice == '5':
            book_id = Prompt.ask("Enter the book ID to update")
            book = library.find_book(book_id)
            if book:
                console.print("[yellow]Which field do you want to update? (e.g., name, writer, rate)[/yellow]")
                key = Prompt.ask("Enter field name")
                value = Prompt.ask(f"Enter the new value for {key}")
                book.update_info(key, value)
            else:
                console.print("[bold red]Error: Book not found.[/bold red]")

        elif choice == '6':
            console.print("\n[bold magenta]Thank you for using me :) [/bold magenta]")
            break
        
        Prompt.ask("\n[dim]Press Enter to return to the menu...[/dim]")
        console.clear()


if __name__ == "__main__":
    interface()