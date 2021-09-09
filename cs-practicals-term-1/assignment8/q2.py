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
