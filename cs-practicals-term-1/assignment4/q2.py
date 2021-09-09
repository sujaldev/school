"""
Write a menu driven Program to Store Name and Phone number in a dictionary, Input Name
and search his/her phone number, Input Phone and search its owner name. Traverse the
whole dictionary depending on choice of the user.
"""
phonebook = {}

while True:
    print("1. Create phonebook",
          "2. Search phone number by name",
          "3. Search name by phone number",
          "4. Exit", sep="\n")
    choice = input("Enter choice: ")

    if choice == "1":
        while input("Enter values (y/n): ").lower() == "y":
            name, number = input("Enter name: "), input("Enter number: ")
            if name not in phonebook.keys():
                phonebook[name] = number
            else:
                print("This name already exists, try again")

    elif choice == "2":
        name = input("Enter name to look for: ")
        if name in phonebook.keys():
            print(f"{name} owns the number {phonebook[name]}")
        else:
            print("No such person exists in record.")

    elif choice == "3":
        number = input("Enter number to look for: ")
        for name, phone in phonebook.items():
            if phone == number:
                print(f"The number {number} belongs to {name}.")
                break
        else:
            print("No such number exists in record.")

    elif choice == "4":
        print("exiting...")
        break

    else:
        print("Invalid choice.")

"""
OUTPUT:
1. Create phonebook
2. Search phone number by name
3. Search name by phone number
4. Exit
Enter choice: 1
Enter values (y/n): y
Enter name: feynman
Enter number: 1234
Enter values (y/n): y
Enter name: turing
Enter number: 4321
Enter values (y/n): n
1. Create phonebook
2. Search phone number by name
3. Search name by phone number
4. Exit
Enter choice: 2
Enter name to look for: turing
turing owns the number 4321
1. Create phonebook
2. Search phone number by name
3. Search name by phone number
4. Exit
Enter choice: 2
Enter name to look for: john
No such person exists in record.
1. Create phonebook
2. Search phone number by name
3. Search name by phone number
4. Exit
Enter choice: 3
Enter number to look for: 1234
The number 1234 belongs to feynman.
1. Create phonebook
2. Search phone number by name
3. Search name by phone number
4. Exit
Enter choice: 3
Enter number to look for: 987967
No such number exists in record.
1. Create phonebook
2. Search phone number by name
3. Search name by phone number
4. Exit
Enter choice: 4
exiting...
"""