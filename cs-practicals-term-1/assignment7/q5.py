"""
Write a menu driven program to do the following:-
   a) To create a binary file ‘item.dat’ containing fields as
      item_id, item_name, price, quantity in the following format:
      [[121,pen,20,5],[21,pencil,10,10],…..]
   b) To display the above file
   c) Add more item details in the existing file.
   d) Display the details of an item for a given item_id.
"""
import pickle


def create():
    data = []
    while input("Enter values (y/n): ").lower() == "y":
        data.append([
            int(input("Enter item id: ")),
            input("Enter item name: "),
            float(input("Enter item price: ")),
            int(input("Enter item quantity: "))
        ])
    file = open("student.dat", "wb")
    pickle.dump(data, file)
    file.close()


def display():
    file = open("student.dat", "rb")
    data = pickle.load(file)
    file.close()
    for item in data:
        print("ITEM ID: {} | ITEM NAME: {} | PRICE: {} | QUANTITY: {}".format(*item))


def append():
    file = open("student.dat", "rb")
    data = pickle.load(file)
    file.close()
    print("ENTER NEW ITEMS")
    while input("Enter values (y/n): ").lower() == "y":
        data.append([
            int(input("Enter item id: ")),
            input("Enter item name: "),
            float(input("Enter item price: ")),
            int(input("Enter item quantity: "))
        ])

    file = open("student.dat", "wb")
    pickle.dump(data, file)
    file.close()


def seek():
    file = open("student.dat", "rb")
    data = pickle.load(file)
    file.close()
    search_id = int(input("Enter search item id: "))
    for item in data:
        current_id = item[0]
        if current_id == search_id:
            print("ITEM ID: {} | ITEM NAME: {} | PRICE: {} | QUANTITY: {}".format(*item))
            break
    else:
        print("NO MATCH FOUND")


def menu():
    while True:
        print("\n"
              "1: Create File",
              "2: Display File",
              "3: Append to file",
              "4: Search for item",
              "5: Exit", sep="\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            create()
        elif choice == "2":
            display()
        elif choice == "3":
            append()
        elif choice == "4":
            seek()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("INVALID CHOICE TRY AGAIN...")


menu()
