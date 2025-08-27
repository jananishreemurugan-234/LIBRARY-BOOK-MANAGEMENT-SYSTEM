import datetime

# ---------- Data ----------
books = {}
issued_books = {}

# ---------- Functions ----------
def add_book():
    book_id = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Author: ")
    quantity = int(input("Enter Quantity: "))
    books[book_id] = {"title": title, "author": author, "quantity": quantity}
    print("Book added successfully!\n")

def remove_book():
    book_id = input("Enter Book ID to remove: ")
    if book_id in books:
        del books[book_id]
        print("Book removed successfully!\n")
    else:
        print("Book not found!\n")

def issue_book():
    book_id = input("Enter Book ID to issue: ")
    if book_id in books and books[book_id]['quantity'] > 0:
        student = input("Enter Student Name: ")
        issue_date = datetime.date.today()
        due_date = issue_date + datetime.timedelta(days=7)
        issued_books[book_id] = {"student": student, "issue_date": issue_date, "due_date": due_date}
        books[book_id]['quantity'] -= 1
        print(f"Book issued to {student}. Due date: {due_date}\n")
    else:
        print("Book not available or does not exist!\n")

def return_book():
    book_id = input("Enter Book ID to return: ")
    if book_id in issued_books:
        return_date = datetime.date.today()
        due_date = issued_books[book_id]['due_date']
        delay = (return_date - due_date).days
        fine = 10 * delay if delay > 0 else 0
        books[book_id]['quantity'] += 1
        del issued_books[book_id]
        print(f"Book returned successfully! Fine: ₹{fine}\n")
    else:
        print("This book was not issued!\n")

def display_books():
    if books:
        for book_id, details in books.items():
            print(f"ID: {book_id}, Title: {details['title']}, Author: {details['author']}, Quantity: {details['quantity']}")
    else:
        print("No books available.")
    print()

# ---------- Main Menu ----------
while True:
    print("\n--- Library Book Management ---")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display Books")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_book()
    elif choice == '2':
        remove_book()
    elif choice == '3':
        issue_book()
    elif choice == '4':
        return_book()
    elif choice == '5':
        display_books()
    elif choice == '6':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again!\n")