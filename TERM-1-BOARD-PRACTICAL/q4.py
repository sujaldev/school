"""
Q4) Write a menu driven program in Python to do the following(using user defined functions) :
    a) to create a text file “MYFILE.TXT” and store strings in it .
    b) display all strings of the text file.
    c) to count the number of words starting with ‘A’ .
"""


def create():
    file = open("MYFILE.TXT", "w")
    while input("Enter lines (y/n): ").lower() == "y":
        file.write(input("Enter string: ") + "\n")
    file.close()


def display():
    print("Contents of the file are as follows:")
    with open("MYFILE.TXT") as file:
        print(file.read())


def count():
    with open("MYFILE.TXT") as file:
        words = file.read().split()
        words = [w for w in words if w[0].upper() == "A"]

    if words:
        print(len(words), " words start with A, these are:\n", "\n".join(words), sep="")
    else:
        print("No word starts with A in this file.")


def menu():
    while True:
        choice = input(
            "\n\n"
            "1. Create file\n"
            "2. Display file\n"
            "3. Count words starting with A\n"
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
