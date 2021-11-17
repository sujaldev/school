"""
Q5) Write a menu driven program in Python to do the following using user defined functions:
    a) to create a text file “DIARY.TXT” and store strings in it .
    b) display all strings of the text file.
    c) to count the no. of “Me” or “My” words present in a text file “DIARY.TXT”.
If the file “DIARY.TXT” content is as follows :
My first book was Me and My family. It gave me a chance to be known to the world.
The output of the function should be
Count of Me/My in file : 4
"""


def create():
    file = open("DIARY.TXT", "w")
    while input("Enter lines (y/n): ").lower() == "y":
        file.write(input("Enter string: ") + "\n")
    file.close()


def display():
    print("Contents of the file are as follows:")
    with open("DIARY.TXT") as file:
        print(file.read())


def count():
    with open("DIARY.TXT") as file:
        data = file.read().split()
        data = [w for w in data if w.lower() in ("me", "my")]

    if data:
        print("Count of Me/My in file:", len(data))
    else:
        print("No instances of Me and My in file.")


def menu():
    while True:
        choice = input(
            "\n\n"
            "1. Create file\n"
            "2. Display file\n"
            "3. Count Me My words\n"
            "4. Exit\n"
            "Enter your choice: "
        )

        if choice == "1":
            create()
        elif choice == "2":
            display()
        elif choice == "3":
            count()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice... Try again...")


menu()
