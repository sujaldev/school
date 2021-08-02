"""
Q18) WAP to menu driven program to do the following:-
a) Create a binary file 'item.dat' consisting of
    item_id, item_name, price, quantity in the following format:
    [[121,pen,20,5],[21,pencil,10,10],.....]
b) Display the above file
c) Add more item details in the existing file
d) Display the details of an item for a given item_id
"""
import pickle


def create():
    wrapper = []
    while input("Enter values (y/n):").lower() == "y":
        wrapper.append([
            int(input("Enter ITEM ID:")),
            input("Enter ITEM NAME:"),
            float(input("Enter ITEM PRICE:")),
            int(input("Enter ITEM QUANTITY:"))
        ])

    file = open("item.dat", "wb")
    pickle.dump(wrapper, file)
    file.close()


def display():
    try:
        file = open("item.dat", "rb")
        for entry in pickle.load(file):
            print(f"\nITEM ID: {entry[0]}",
                  f"ITEM NAME: {entry[1]}",
                  f"ITEM PRICE: {entry[2]}",
                  f"ITEM QUANTITY: {entry[3]}\n", sep="\n")
    except FileNotFoundError:
        print("\nFILE DOES NOT EXIST YET! CREATE FILE FIRST\n")


def item_append():
    try:
        file = open("item.dat", "rb")
        data = pickle.load(file)
        file.close()

        while input("Enter values (y/n):").lower() == "y":
            data.append([
                int(input("Enter ITEM ID:")),
                input("Enter ITEM NAME:"),
                float(input("Enter ITEM PRICE:")),
                int(input("Enter ITEM QUANTITY:"))
            ])

        file = open("item.dat", "wb")
        pickle.dump(data, file)
        file.close()
    except FileNotFoundError:
        print("\nFILE DOES NOT EXIST YET! CREATE THE FILE FIRST\n")


def lookup():
    try:
        file = open("item.dat", "rb")
        item_id = int(input("Enter ITEM ID to look for: "))
        match = []
        for entry in pickle.load(file):
            if item_id == entry[0]:
                match = entry
                break
        file.close()

        if match:
            print(f"\nITEM ID: {match[0]}",
                  f"ITEM NAME: {match[1]}",
                  f"ITEM PRICE: {match[2]}",
                  f"ITEM QUANTITY: {match[3]}\n", sep="\n")
        else:
            print("\nMATCH NOT FOUND\n")
    except FileNotFoundError:
        print("\nFILE DOES NOT EXIST YET! CREATE THE FILE FIRST\n")


def menu():
    while True:
        print("1: CREATE FILE",
              "2: DISPLAY FILE",
              "3: ADD MORE ITEMS",
              "4: LOOKUP ITEM",
              "5: EXIT", sep="\n")

        choice = input("ENTER CHOICE: ")

        if choice == "1":
            create()
        elif choice == "2":
            display()
        elif choice == "3":
            item_append()
        elif choice == "4":
            lookup()
        elif choice == "5":
            break
        else:
            print("INVALID CHOICE TRY AGAIN...")


menu()
