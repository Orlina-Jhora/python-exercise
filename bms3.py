# Operation 3

books = [
    {"book_name": "Python Basics", "book_qty": 10},
    {"book_name": "Clean Code", "book_qty": 5}
]


# Find a book by name
def find_book(name):
    for book in books:
        if book["book_name"].lower() == name.lower():
            return book
    return None


# Sell book function
def sell_book(name, qty):

    # Step 1: Find the book
    book = find_book(name)

    if book is None:
        print(f"Error: '{name}' not found!")
        return

    # Step 2: Validate quantity
    if qty <= 0:
        print("Error: Quantity must be greater than 0!")
        return

    # Step 3: Check available stock
    if book["book_qty"] < qty:
        print("Error: Not enough stock available!")
        print("Available Stock:", book["book_qty"])
        return

    # Step 4: Deduct quantity
    book["book_qty"] -= qty
    # Same as:
    # book["book_qty"] = book["book_qty"] - qty

    # Step 5: Print confirmation
    print("Book Sold Successfully!")
    print("Name      :", name)
    print("Sold Qty  :", qty)
    print("Remaining :", book["book_qty"])



sell_book("Python Basics", 3)
print()

sell_book("Python Basics", 20)
print()

sell_book("Java", 2)