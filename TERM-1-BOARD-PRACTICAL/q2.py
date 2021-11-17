"""
Q2) A school maintains a binary file that contains following information for every student: roll
number, name, marks and grade. Write a program in Python to do the following (using user defined
functions):
    a) Create the file of students [student.dat]
    b) Display the records of all ‘A’ grade students.
"""
import pickle


def create():
    # COLLECT USER INPUT
    data = []
    while input("Enter values (y/n): ").lower() == "y":
        data.append([
            int(input("Enter roll number: ")),
            input("Enter student name: "),
            float(input("Enter marks: ")),
            input("Enter grade: ").upper()
        ])

    # (CREATE AND) WRITE TO BINARY FILE
    with open("student.dat", "wb") as db:
        pickle.dump(data, db)


def display():
    with open("student.dat", "rb") as db:
        data = pickle.load(db)

    a_graders = [f"{s[1]} ({s[0]})" for s in data if s[-1] == "A"]
    if a_graders:
        print("Students with A grade:", *a_graders, sep="\n")
    else:
        print("No toppers in this stupid class.")


def menu():
    while True:
        choice = input(
            "\n\n"
            "1. Create student database\n"
            "2. Display students with A grade\n"
            "3. Exit\n"
            "Enter your choice: "
        )

        if choice == "1":
            create()
        elif choice == "2":
            display()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice... Try again...")


menu()
