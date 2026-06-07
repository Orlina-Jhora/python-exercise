#operation 4

# Book inventory
books = [
    {"book_name": "Python Basics", "book_qty": 10},
    {"book_name": "Clean Code", "book_qty": 5}
]


# Find a book
def find_book(name):
    for book in books:
        if book["book_name"].lower() == name.lower():
            return book
    return None


# Restock function
def add_book_qty(name, qty):

    # Step 1: Find the book
    book = find_book(name)

    if book is None:
        print(f"Error: '{name}' not found! Create it first.")
        return

    # Step 2: Validate quantity
    if qty <= 0:
        print("Error: Quantity must be greater than 0!")
        return

    # Step 3: Add quantity to stock
    book["book_qty"] += qty

    # Step 4: Print confirmation
    print(f"Restocked '{name}' by {qty}. New total: {book['book_qty']}")



add_book_qty("Python Basics", 5)
print()

add_book_qty("Unknown Book", 5)