"""
5) [PRACTICAL] Write a menu driven program to do the following:-
   a) To create a binary file 'student.dat' containing fields as rno, name, marks and grade in a list.
   b) Function to delete a record for a given roll number.
   b) Display the file after and before updating
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
    try:
        file = open("student.dat", "rb")
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


def delete():
    db = read()
    file = open("student.dat", "wb")
    roll_no = int(input("Enter roll number to look for: "))
    matched = False

    for student in db:
        print("OLD: ", f"{student[1]} with roll number {student[0]} has grade {student[2]}")
        if student[0] == roll_no:
            continue
        print("NEW: ", f"{student[1]} with roll number {student[0]} has grade {student[2]}")
        pickle.dump(student, file)
    file.close()

    if not matched:
        print("NO MATCH FOUND, NOT UPDATED")


def menu():
    while True:
        print("\n"
              "1: Create File",
              "2: Delete Roll Number",
              "3: Exit", sep="\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            create()
        elif choice == "2":
            delete()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("INVALID CHOICE TRY AGAIN...")


menu()
