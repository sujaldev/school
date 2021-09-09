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