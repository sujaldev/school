"""
Q3)[PRACTICAL] Write a menu driven program to do the following:-
   a) To create a binary file 'product.dat' in the following format :
    {‘name’ : ‘file’, ‘price’ : 113}, {‘name’ : ‘pen’, ‘price’ : 30}, etc.
   b) To display the above file
   c) Transfer all the records from binary file ‘product.dat’ to ‘new.dat’ whose price is less than 101.
"""
import pickle


def create():
    file = open("product.dat", "wb")
    while input("Enter values (y/n): ").lower() == "y":
        print()
        pickle.dump({
            "name": input("Enter product name: "),
            "price": float(input("Enter price: "))
        }, file)
    file.close()


def read(file_name):
    try:
        file = open(file_name, "rb")
    except FileNotFoundError:
        print("FILE DOES NOT EXIST, CREATE IT FIRST.")
        return []

    buffer = []
    try:
        while True:
            buffer.append(pickle.load(file))
    except EOFError:
        file.close()
        return buffer


def display():
    db = read("product.dat")
    for item in db:
        print(f"cost of 1 {item['name']} is {item['price']}")


def transfer():
    new_file = open("new.dat", "wb")
    db = read("product.dat")
    for item in db:
        if item["price"] < 100:
            pickle.dump(item, new_file)
    new_file.close()


def display_transferred():
    db = read("new.dat")
    for item in db:
        print(f"cost of 1 {item['name']} is {item['price']}")


def menu():
    while True:
        print("\n"
              "1: Create File",
              "2: Display File",
              "3: Transfer Cheap",
              "4: Display New File",
              "5: Exit", sep="\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            create()
        elif choice == "2":
            display()
        elif choice == "3":
            transfer()
        elif choice == "4":
            display_transferred()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("INVALID CHOICE TRY AGAIN...")


menu()
