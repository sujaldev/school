"""
Q1) A blood bank maintains a binary file that contains following information for every donor: name,
date of birth, address, phone number and blood group. Write a program in Python to do the following
(using user defined functions):
    a) Create the file of donors [donor.dat]
    b) Display the records.
    c) For Input of a specific blood group, display the name and address of donors of
     that blood group.
"""
import pickle


def create():
    # COLLECT USER INPUT
    data = []
    while input("Enter values (y/n): ").lower() == "y":
        data.append([
            input("Enter donor name: "),
            input("Enter DOB (dd/mm/yyyy): "),
            input("Enter address: "),
            input("Enter phone number: "),
            input("Enter blood group: ")
        ])

    # (CREATE AND) WRITE TO BINARY FILE
    with open("donor.dat", "wb") as db:
        pickle.dump(data, db)


def display():
    with open("donor.dat", "rb") as db:
        data = pickle.load(db)

    template = "| {:^20} || {:^20} || {:^20} || {:^20} || {:^20} |"
    for donor in data:
        print(template.format(*donor))


def seek():
    with open("donor.dat", "rb") as db:
        data = pickle.load(db)

    wanted_group = input("Enter the desired blood group: ")
    for donor in data:
        if donor[-1] == wanted_group:
            print(
                f"Name: {donor[0]}",
                f"Address: {donor[2]}\n", sep="\n"
            )


def menu():
    while True:
        choice = input(
            "\n\n"
            "1. Create donor database\n"
            "2. Display donor records\n"
            "3. Find Donor by blood group\n"
            "4. Exit\n"
            "Enter your choice: "
        )

        if choice == "1":
            create()
        elif choice == "2":
            display()
        elif choice == "3":
            seek()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice... Try again...")


menu()
