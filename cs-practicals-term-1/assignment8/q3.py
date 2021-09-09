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
