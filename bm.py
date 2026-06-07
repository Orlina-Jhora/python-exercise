#Book Management System

#Book-List

# books =[
#     "Python Basics",
#     "Data Structures",
#     "Machine Learning",
#     "Clean Code"
# 
# ]
# print( books)
# print(books[2])
# print(books[0:3])
# for book in books:
#print( books)

#Dictionary

# books = {
#     "name":"Python Basics", "quantity": 10,
#     "name": "Data Structures", "quantity": 5,
#     "name": "Machine Learning", "quantity": 8,
#     "name": "Clean Code", "quantity": 12
}
#     print(book)
    # print(book["name"])
    # print(book["quantity"])

#List of Dictionaries
# books = [
#     {"name":"Python Basics", "quantity": 10},
#     {"name": "Data Structures", "quantity": 5},
#     {"name": "Machine Learning", "quantity": 8},
#     {"name": "Clean Code", "quantity": 12}
# ]
#print(books[1]["name"])

#Loop
# for book in books:
    #book_dict=book
#print( books(book_dict["name"])

#Append

# books.append({"name": "Basic C", "quantity": 10})
# books.append({"name": "Basic PHP", "quantity": 5})
# books.append({"name": "Excel Advanced", "quantity": 8})
# books.append({"name": "Basic Photoshop", "quantity": 12})

#print(books)


#search-book

# search= input("Enter book name:")

# for book in books:
#     if book["name"] == search:
#         print("Found:")  
 
#7
# book = {"name": "Python Basics", "quantity": 10}

# book["quantity"] = 15

# print(book)

#8
# books = [
#     {"name": "Python Basics", "quantity": 10},
#     {"name": "Data Structures", "quantity": 5},
#     {"name": "Machine Learning", "quantity": 8},
#     {"name": "Clean Code", "quantity": 12}
# ]

# def add_book(name, quantity):
#     books.append({"name": name, "quantity": quantity})

# add_book("Python Advanced", 10)
# add_book("Java", 5)

# for book in books:
#     print(book["name"], "-", book["quantity"])

#9
# def get_book_quantity(name):
#     books = {
#         "Python Basics": 10,
#         "Java": 5
#     }
#     return books[name]

# print(get_book_quantity("Python Basics"))

#Book Menu

# books = [
#     {"name":"Python Basics", "quantity": 10},
#     {"name": "Data Structures", "quantity": 5},
#     {"name": "Machine Learning", "quantity": 8},
#     {"name": "Clean Code", "quantity": 12}
# ]

# while True:
#     print("\n--- Book Menu ---")
#     print("1. Create New Books")
#     print("2. List of Books")
#     print("3. Sell a book")
#     print("4. Update book of qty")
#    print("5. Exit")
#     choice = input("Enter your choice: ")

#     if choice == "1":
#         name = input("Enter book name: ")
#         qty = int(input("Enter quantity: "))
#         books.append({"name": name, "quantity": qty})

#     elif choice == "2":
#         for book in books:
#             print(book["name"])

#     elif choice == "3":
#         name = input("Enter book name to search: ")
#         found = False

#         for book in books:
#             if book["name"] == name:
#                 print("Quantity:", book["quantity"])
#                 found = True
#                 break

#         if not found:
#             print("Book not found")

#     elif choice == "4":
#         print("Exiting...")
#         break

#     else:
#         print("Invalid choice")
