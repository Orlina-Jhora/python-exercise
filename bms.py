#operation 1

books = [
    {"book_name": "Python Basics",  "book_qty": 10},
       {"book_name": "Clean Code",     "book_qty": 5},
       {"book_name": "The Pragmatic",  "book_qty": 8},
]

#Step 1
def find_book(name):
    for book in books:
        if book["book_name"].lower() == name.lower():
            return book
    return None

def create_book(name, qty):
   
    if find_book(name):
        print(f"Error: '{name}' already exists!")
        return

#     # Step 2: Validate quantity
    if qty <= 0:
        print("Error: Quantity must be greater than 0!")
        return

#     # Step 3: Create new dictionary
    new_book = {
        "book_name": name,
        "book_qty": qty
    }

#     # Step 4: Add to books list
    books.append(new_book)

    # Step 5: Success message
    print("Book Added Successfully!")
    print("Name     :", name)
    print("Quantity :", qty)

create_book("Clean Code", 10)
print()

create_book("Python Advanced", 5)