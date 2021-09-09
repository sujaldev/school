"""
Write a menu driven program to do the following:
    a) Create a csv file 'book.csv' containing book record as book_no, book_name, author_name and cost.
    b) Display the file.
    c) Update the details of a book for the given book number.
"""
import csv


def create():
    book = open("book.csv", "w")
    writer = csv.writer(book)
    while input("Enter a record (y/n): ").lower() == "y":
        writer.writerow([
            input("Enter book no: "),
            input("Enter book name: "),
            input("Enter author name: "),
            input("Enter cost: ")
        ])
    book.close()


def display():
    book = open("book.csv")
    rows = csv.reader(book)
    print(f"| {'BOOK NUMBER' :^20} | {'BOOK NAME' :^20} | {'AUTHOR NAME' :^20} | {'COST' :^20} |")
    for row in rows:
        print("| {:^20} | {:^20} | {:^20} | {:^20} |".format(*row))
    book.close()


def read():
    book = open("book.csv")
    rows = [r for r in csv.reader(book)]
    book.close()
    return rows


def update():
    rows, match = read(), False
    book, search_no = open("book.csv", "w"), input("Enter search book no: ")
    writer = csv.writer(book)
    for row in rows:
        current_book_no = row[0]
        if current_book_no == search_no:
            match = True
            print("Record Found, Update now")
            writer.writerow([
                input("Enter book no: "),
                input("Enter book name: "),
                input("Enter author name: "),
                input("Enter cost: ")
            ])
        else:
            writer.writerow(row)
    if not match:
        print("No match was found!")
    book.close()


def menu():
    while True:
        print("1. Create File",
              "2. Display",
              "3. Update"
              "4. Exit", sep="\n")
        choice = input("Enter choice: ")

        if choice == "1":
            create()
        elif choice == "2":
            display()
        elif choice == "3":
            update()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again...")


menu()
