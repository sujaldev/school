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

"""
OUTPUT:
1: Create File
2: Display File
3: Append to file
4: Search for item
5: Exit
Enter your choice: 1
Enter values (y/n): y
Enter item id: 1
Enter item name: pen
Enter item price: 10
Enter item quantity: 100
Enter values (y/n): y
Enter item id: 2
Enter item name: pencil
Enter item price: 5
Enter item quantity: 2000
Enter values (y/n): n

1: Create File
2: Display File
3: Append to file
4: Search for item
5: Exit
Enter your choice: 2
ITEM ID: 1 | ITEM NAME: pen | PRICE: 10.0 | QUANTITY: 100
ITEM ID: 2 | ITEM NAME: pencil | PRICE: 5.0 | QUANTITY: 2000

1: Create File
2: Display File
3: Append to file
4: Search for item
5: Exit
Enter your choice: 3
ENTER NEW ITEMS
Enter values (y/n): y
Enter item id: 3
Enter item name: geometry box
Enter item price: 200
Enter item quantity: 20
Enter values (y/n): n

1: Create File
2: Display File
3: Append to file
4: Search for item
5: Exit
Enter your choice: 2
ITEM ID: 1 | ITEM NAME: pen | PRICE: 10.0 | QUANTITY: 100
ITEM ID: 2 | ITEM NAME: pencil | PRICE: 5.0 | QUANTITY: 2000
ITEM ID: 3 | ITEM NAME: geometry box | PRICE: 200.0 | QUANTITY: 20

1: Create File
2: Display File
3: Append to file
4: Search for item
5: Exit
Enter your choice: 4
Enter search item id: 3
ITEM ID: 3 | ITEM NAME: geometry box | PRICE: 200.0 | QUANTITY: 20

1: Create File
2: Display File
3: Append to file
4: Search for item
5: Exit
Enter your choice: 4
Enter search item id: 98
NO MATCH FOUND

1: Create File
2: Display File
3: Append to file
4: Search for item
5: Exit
Enter your choice: 5
Exiting...
"""
