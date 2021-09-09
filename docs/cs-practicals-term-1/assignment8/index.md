# SCHOOL RESOURCES ARCHIVE

All school related resources stored here.

#### THIS WEBSITE IS MAINTAINED BY SUJAL SINGH

### RESOURCE LIST

## <br>Write a menu driven program to do the following:<br>    a) Create a csv file 'book.csv' containing book record as book_no, book_name, author_name and cost.<br>    b) Display the file.<br>    c) Update the details of a book for the given book number.<br>
```python
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

```
## <br>Write a menu driven program to do the following :<br>    a) Create a csv file 'item.csv' containing item record as item_no, item_name, cost and quantity.<br>    b) Display the file.<br>    c) Delete an item where the item number is given by the user.<br>
```python
"""
Write a menu driven program to do the following :
    a) Create a csv file 'item.csv' containing item record as item_no, item_name, cost and quantity.
    b) Display the file.
    c) Delete an item where the item number is given by the user.
"""
import csv


def create():
    item_file = open("item.csv", "w")
    writer = csv.writer(item_file)
    while input("Enter a record (y/n): ").lower() == "y":
        writer.writerow([
            input("Enter item no: "),
            input("Enter item name: "),
            input("Enter cost: "),
            input("Enter quantity: ")
        ])
    item_file.close()


def display():
    item_file = open("book.csv")
    rows = csv.reader(item_file)
    print(f"| {'ITEM NUMBER' :^20} | {'ITEM NAME' :^20} | {'ITEM COST' :^20} | {'ITEM QUANTITY' :^20} |")
    for row in rows:
        print("| {:^20} | {:^20} | {:^20} | {:^20} |".format(*row))
    item_file.close()


def read():
    item_file = open("book.csv")
    rows = [r for r in csv.reader(item_file)]
    item_file.close()
    return rows


def delete():
    rows, match = read(), False
    item_file, search_no = open("book.csv", "w"), input("Enter search item no: ")
    writer = csv.writer(item_file)
    for row in rows:
        current_item_no = row[0]
        if current_item_no == search_no:
            match = True
            print("Record Found and deleted")
        else:
            writer.writerow(row)
    if not match:
        print("No match was found!")
    item_file.close()


def menu():
    while True:
        print("1. Create File",
              "2. Display",
              "3. Delete"
              "4. Exit", sep="\n")
        choice = input("Enter choice: ")

        if choice == "1":
            create()
        elif choice == "2":
            display()
        elif choice == "3":
            delete()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again...")


menu()

```
## <br>WAF to search and display the record of that product from the file ‘product.csv’ which has<br>maximum cost.<br>Sample of ‘product.csv’ is shown below :<br>PID, PNAME, COST, QUANTITY<br>P1, BRUSH, 50, 200<br>P2, TOOTHPASTE, 120, 150<br>P3, COMB, 40, 300<br>P4, SHEETS, 100, 500<br>
```python
"""
WAF to search and display the record of that product from the file ‘product.csv’ which has
maximum cost.
Sample of ‘product.csv’ is shown below :
PID, PNAME, COST, QUANTITY
P1, BRUSH, 50, 200
P2, TOOTHPASTE, 120, 150
P3, COMB, 40, 300
P4, SHEETS, 100, 500
"""
import csv


def create():
    product_file = open("product.csv", "w")
    writer = csv.writer(product_file)
    writer.writerow(["PID", "PNAME", "COST", "QUANTITY"])
    while input("Enter values (y/n): ").lower() == "y":
        writer.writerow([
            input("Enter product id: "),
            input("Enter product name: "),
            input("Enter product cost: "),
            input("Enter product quantity: ")
        ])
    product_file.close()


def read():
    product_file = open("product.csv")
    rows = [r for r in csv.reader(product_file)]
    product_file.close()
    return rows


def display():
    rows = read()
    for row in rows:
        print("| {:^20} | {:^20} | {:^20} | {:^20} |".format(*row))


def max_search():
    rows = read()
    print("| {: ^20} | {: ^20} | {: ^20} | {: ^20} |".format(*rows[0]))

    max_record = ["", "", "0", ""]
    for row in rows[1:]:  # [1:] to skip header
        current_price = int(row[2])
        if int(max_record[2]) < current_price:
            max_record = row
    print("| {: ^20} | {: ^20} | {: ^20} | {: ^20} |".format(*max_record))


def menu():
    while True:
        print("1. Create File",
              "2. Display",
              "3. Find maximum",
              "4. Exit", sep="\n")
        choice = input("Enter choice: ")

        if choice == "1":
            create()
        elif choice == "2":
            display()
        elif choice == "3":
            max_search()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again...")


menu()

```
## <br>WAF to transfer only those records from the file product.csv to another file ‘pro1.csv’ whose<br>quantity is more than 150. Also include the first row with headings sample of product.csv is<br>shown below :<br>PID, PNAME, COST, QUANTITY<br>P1, BRUSH, 50, 200<br>P2, TOOTHPASTE, 120, 150<br>P3, COMB, 40, 300<br>P4, SHEETS, 100, 500<br>
```python
"""
WAF to transfer only those records from the file product.csv to another file ‘pro1.csv’ whose
quantity is more than 150. Also include the first row with headings sample of product.csv is
shown below :
PID, PNAME, COST, QUANTITY
P1, BRUSH, 50, 200
P2, TOOTHPASTE, 120, 150
P3, COMB, 40, 300
P4, SHEETS, 100, 500
"""
import csv


def read():
    product_file = open("pro1.csv")
    rows = [r for r in csv.reader(product_file)]
    product_file.close()
    return rows


def transfer():
    rows = read()[1:]  # [1:] to skip header
    pro1 = open("pro1.csv", "w")
    writer = csv.writer(pro1)
    writer.writerow(["PID", "PNAME", "COST", "QUANTITY"])
    writer.writerows([r for r in rows if int(r[2]) > 150])
    pro1.close()
    print("Transferred successfully")


def display():
    rows = read()
    for row in rows:
        print("| {:^20} | {:^20} | {:^20} | {:^20} |".format(*row))


def menu():
    while True:
        print("1. Transfer",
              "2. Display",
              "3. Exit", sep="\n")
        choice = input("Enter choice: ")

        if choice == "1":
            transfer()
        elif choice == "2":
            display()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again...")


menu()

```


---

### [RAISE AN ISSUE](https://github.com/sujaldev/school/issues/new/choose) ON GITHUB IF

- Answer is wrong
- Want a missing question to be added
- Need help with a question
- Need help navigating the website
- Website has a bug

### WANT TO CONTRIBUTE RESOURCES?

Fork my [repository](https://github.com/sujaldev/school) \
After adding changes, create a pull request.