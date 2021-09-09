"""
Write a menu driven program to do the following:
    a) Create a csv file 'book.csv' containing book record as book_no, book_name, author_name and cost.
    b) Display the file.
    c) Update the details of a book for the given book number.
"""
import csv


def create():
    book = open("book.csv", "w", newline="")
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
    book = open("book.csv", newline="")
    rows = csv.reader(book)
    print(f"| {'BOOK NUMBER' :^20} | {'BOOK NAME' :^20} | {'AUTHOR NAME' :^20} | {'COST' :^20} |")
    for row in rows:
        print("| {:^20} | {:^20} | {:^20} | {:^20} |".format(*row))
    book.close()


def read():
    book = open("book.csv", newline="")
    rows = [r for r in csv.reader(book)]
    book.close()
    return rows


def update():
    rows, match = read(), False
    book, search_no = open("book.csv", "w", newline=""), input("Enter search book no: ")
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
              "3. Update",
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

"""
OUTPUT:
1. Create File
2. Display
3. Update
4. Exit
Enter choice: 1
Enter a record (y/n): y
Enter book no: 1
Enter book name: book1
Enter author name: author2
Enter cost: 100
Enter a record (y/n): y
Enter book no: 2
Enter book name: book2
Enter author name: author2
Enter cost: 200
Enter a record (y/n): n
1. Create File
2. Display
3. Update
4. Exit
Enter choice: 2
|     BOOK NUMBER      |      BOOK NAME       |     AUTHOR NAME      |         COST         |
|          1           |        book1         |       author2        |         100          |
|          2           |        book2         |       author2        |         200          |
1. Create File
2. Display
3. Update
4. Exit
Enter choice: 3
Enter search book no: 5
No match was found!
1. Create File
2. Display
3. Update
4. Exit
Enter choice: 3
Enter search book no: 2
Record Found, Update now
Enter book no: 3
Enter book name: book3
Enter author name: author3
Enter cost: 300
1. Create File
2. Display
3. Update
4. Exit
Enter choice: 2
|     BOOK NUMBER      |      BOOK NAME       |     AUTHOR NAME      |         COST         |
|          1           |        book1         |       author2        |         100          |
|          3           |        book3         |       author3        |         300          |
1. Create File
2. Display
3. Update
4. Exit
Enter choice: 7
Invalid choice, try again...
1. Create File
2. Display
3. Update
4. Exit
Enter choice: 4
Exiting...
"""
