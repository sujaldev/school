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
    item_file = open("item.csv", "w", newline="")
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
    item_file = open("item.csv", newline="")
    rows = csv.reader(item_file)
    print(f"| {'ITEM NUMBER' :^20} | {'ITEM NAME' :^20} | {'ITEM COST' :^20} | {'ITEM QUANTITY' :^20} |")
    for row in rows:
        print("| {:^20} | {:^20} | {:^20} | {:^20} |".format(*row))
    item_file.close()


def read():
    item_file = open("item.csv", newline="")
    rows = [r for r in csv.reader(item_file)]
    item_file.close()
    return rows


def delete():
    rows, match = read(), False
    item_file, search_no = open("item.csv", "w", newline=""), input("Enter search item no: ")
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
              "3. Delete",
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


"""
OUTPUT:
1. Create File
2. Display
3. Delete
4. Exit
Enter choice: 1
Enter a record (y/n): y
Enter item no: 1
Enter item name: pen
Enter cost: 10
Enter quantity: 100
Enter a record (y/n): y
Enter item no: 2
Enter item name: pencil
Enter cost: 5
Enter quantity: 2000
Enter a record (y/n): n
1. Create File
2. Display
3. Delete
4. Exit
Enter choice: 2
|     ITEM NUMBER      |      ITEM NAME       |      ITEM COST       |    ITEM QUANTITY     |
|          1           |         pen          |          10          |         100          |
|          2           |        pencil        |          5           |         2000         |
1. Create File
2. Display
3. Delete
4. Exit
Enter choice: 3
Enter search item no: 2938
No match was found!
1. Create File
2. Display
3. Delete
4. Exit
Enter choice: 3
Enter search item no: 1
Record Found and deleted
1. Create File
2. Display
3. Delete
4. Exit
Enter choice: 2
|     ITEM NUMBER      |      ITEM NAME       |      ITEM COST       |    ITEM QUANTITY     |
|          2           |        pencil        |          5           |         2000         |
1. Create File
2. Display
3. Delete
4. Exit
Enter choice: 4
Exiting...
"""
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
    product_file = open("product.csv", "w", newline="")
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
    product_file = open("product.csv", newline="")
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

"""
OUTPUT:
1. Create File
2. Display
3. Find maximum
4. Exit
Enter choice: 1
Enter values (y/n): y
Enter product id: p1
Enter product name: pen
Enter product cost: 10
Enter product quantity: 100
Enter values (y/n): y
Enter product id: p2
Enter product name: pencil
Enter product cost: 5
Enter product quantity: 2000
Enter values (y/n): n
1. Create File
2. Display
3. Find maximum
4. Exit
Enter choice: 2
|         PID          |        PNAME         |         COST         |       QUANTITY       |
|          p1          |         pen          |          10          |         100          |
|          p2          |        pencil        |          5           |         2000         |
1. Create File
2. Display
3. Find maximum
4. Exit
Enter choice: 3
|         PID          |        PNAME         |         COST         |       QUANTITY       |
|          p1          |         pen          |          10          |         100          |
1. Create File
2. Display
3. Find maximum
4. Exit
Enter choice: 4
Exiting...
"""

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


def read(file_name="product"):
    product_file = open(f"{file_name}.csv", newline="")
    rows = [r for r in csv.reader(product_file)]
    product_file.close()
    return rows


def transfer():
    rows = read()[1:]  # [1:] to skip header
    pro1 = open("pro1.csv", "w", newline="")
    writer = csv.writer(pro1)
    writer.writerow(["PID", "PNAME", "COST", "QUANTITY"])
    writer.writerows([r for r in rows if int(r[2]) > 150])
    pro1.close()
    print("Transferred successfully")


def display():
    rows = read("pro1")
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


"""
OUTPUT:
1. Transfer
2. Display
3. Exit
Enter choice: 1
Transferred successfully
1. Transfer
2. Display
3. Exit
Enter choice: 2
|         PID          |        PNAME         |         COST         |       QUANTITY       |
|          p3          |     geometry box     |         500          |          20          |
1. Transfer
2. Display
3. Exit
Enter choice: 3
Exiting...
"""
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

<script src="https://giscus.app/client.js"
        data-repo="sujaldev/school"
        data-repo-id="MDEwOlJlcG9zaXRvcnkzODUzMDMzOTI="
        data-category="Q&A"
        data-category-id="DIC_kwDOFvdDYM4CArKZ"
        data-mapping="pathname"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-theme="light"
        data-lang="en"
        crossorigin="anonymous"
        async>
</script>