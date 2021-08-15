"""
2) [PRACTICAL] Write a menu driven program to do the following functions:-
a) To create a binary file 'student.dat' containing fields as rno, name, marks and grade in a list.
b) Display the details of all those students who have got grade A.
"""
import pickle


def create():
    file = open("student.dat", "wb")
    while input("Enter values (y/n): ").lower() == "y":
        print()
        pickle.dump([
            int(input("Enter roll number: ")),
            input("Enter student's name: "),
            input("Enter student's grade: ")
        ], file)
    file.close()


def read():
    file = open("student.dat", "rb")
    buffer = []
    try:
        while True:
            buffer.append(pickle.load(file))
    except EOFError:
        file.close()
        return buffer


def display_toppers():
    toppers = "\n".join([f"Roll No: {s[0]}\nName: {s[1]}" for s in read() if s[-1] == "A"])
    if not toppers:
        print("No toppers in this stupid class.")
    else:
        print(toppers)


def menu():
    while True:
        print("\n"
              "1: Create File",
              "2: Display Toppers",
              "3: Exit", sep="\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            create()
        elif choice == "2":
            display_toppers()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("INVALID CHOICE TRY AGAIN...")


menu()
