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
