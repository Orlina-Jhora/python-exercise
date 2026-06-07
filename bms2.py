#Operation 2

# Book inventory list
books = [
    {"book_name": "Python Basics", "book_qty": 10},
    {"book_name": "Clean Code", "book_qty": 5}
]


def list_books():
    # Step 1: Check if list is empty
    if len(books) == 0:
        print("No books available in inventory!")
        return

    # Header
    print("-" * 47)
    print(f"{'#':<5}{'Book Name':<30}{'Qty'}")
    print("-" * 47)

    # Step 2 & 3: Loop using enumerate()
    total_stock = 0

    for index, book in enumerate(books, start=1):
        print(f"{index:<5}{book['book_name']:<30}{book['book_qty']}")
        total_stock += book["book_qty"]

    # Step 4: Print totals
    print("-" * 47)
    print(f"Total books: {len(books)}  |  Total stock: {total_stock}")


list_books()