# ==========================================
# BOOK INVENTORY MANAGEMENT SYSTEM
# ==========================================

# Global book list
books = []


# ==========================================
# FIND BOOK
# ==========================================
def find_book(name):
    for book in books:
        if book["book_name"].lower() == name.lower():
            return book
    return None


# ==========================================
# OPERATION 1: CREATE BOOK
# ==========================================
def create_book(name, qty):

    # Check if book already exists
    if find_book(name):
        print(f"\nError: '{name}' already exists!")
        return

    # Validate quantity
    if qty <= 0:
        print("\nError: Quantity must be greater than 0!")
        return

    # Create dictionary
    new_book = {
        "book_name": name,
        "book_qty": qty
    }

    # Add to list
    books.append(new_book)

    # Success message
    print("\nBook Added Successfully!")
    print("Name     :", name)
    print("Quantity :", qty)


# ==========================================
# OPERATION 2: LIST BOOKS
# ==========================================
def list_books():

    if len(books) == 0:
        print("\nNo books available in inventory!")
        return

    print("\n" + "-" * 47)
    print(f"{'#':<5}{'Book Name':<30}{'Qty'}")
    print("-" * 47)

    total_stock = 0

    for index, book in enumerate(books, start=1):
        print(f"{index:<5}{book['book_name']:<30}{book['book_qty']}")
        total_stock += book["book_qty"]

    print("-" * 47)
    print(f"Total books: {len(books)} | Total stock: {total_stock}")


# ==========================================
# OPERATION 3: SELL BOOK
# ==========================================
def sell_book(name, qty):

    # Find book
    book = find_book(name)

    if book is None:
        print(f"\nError: '{name}' not found!")
        return

    # Validate quantity
    if qty <= 0:
        print("\nError: Quantity must be greater than 0!")
        return

    # Check stock
    if book["book_qty"] < qty:
        print("\nError: Not enough stock available!")
        print("Available Stock:", book["book_qty"])
        return

    # Deduct stock
    book["book_qty"] -= qty

    # Success message
    print("\nBook Sold Successfully!")
    print("Name      :", name)
    print("Sold Qty  :", qty)
    print("Remaining :", book["book_qty"])


# ==========================================
# OPERATION 4: ADD BOOK QUANTITY
# ==========================================
def add_book_qty(name, qty):

    # Find book
    book = find_book(name)

    if book is None:
        print(f"\nError: '{name}' not found! Create it first.")
        return

    # Validate quantity
    if qty <= 0:
        print("\nError: Quantity must be greater than 0!")
        return

    # Add stock
    book["book_qty"] += qty

    # Success message
    print(f"\nRestocked '{name}' by {qty}.")
    print("New total:", book["book_qty"])


# ==========================================
# MENU SYSTEM
# ==========================================
while True:

    print("\n========== BOOK INVENTORY MENU ==========")
    print("1. Create Book")
    print("2. List Books")
    print("3. Sell Book")
    print("4. Restock Book")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    # Create Book
    if choice == "1":
        name = input("Enter Book Name: ")
        qty = int(input("Enter Quantity: "))
        create_book(name, qty)

    # List Books
    elif choice == "2":
        list_books()

    # Sell Book
    elif choice == "3":
        name = input("Enter Book Name: ")
        qty = int(input("Enter Quantity to Sell: "))
        sell_book(name, qty)

    # Restock Book
    elif choice == "4":
        name = input("Enter Book Name: ")
        qty = int(input("Enter Quantity to Add: "))
        add_book_qty(name, qty)

    # Exit
    elif choice == "5":
        print("\nThank you for using Book Inventory System!")
        break

    else:
        print("\nInvalid Choice! Please try again.")