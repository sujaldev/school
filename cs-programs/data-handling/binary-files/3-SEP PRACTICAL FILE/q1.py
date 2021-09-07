"""
Q1) Write a menu driven program to do the following functions:-
    a) To create a binary file ‘student.dat’ containing fields as rno, name, marks and grade in a list.
    b) Display the details of all those students who have got grade A.
"""
import pickle


def create():
    file = open("student.dat", "wb")

    while input("Add values (y/n): ").lower() == "y":
        pickle.dump([
            int(input("Enter roll no: ")),
            input("Enter student name: "),
            int(input("Enter student's marks: ")),
            input("Enter student's grade: ")
        ], file)

    file.close()


def display():
    file = open("student.dat", "rb")
    matched = False
    try:
        while True:
            student = pickle.load(file)
            grade = student[-1]
            if grade.lower() == "a":
                matched = True
                print("Roll No: {} | Student Name: {} | Marks: {} | Grades: {}".format(*student))
    except EOFError:
        if not matched:
            print("NO GRADE A STUDENTS EXIST")
        file.close()


def menu():
    while True:
        print("\n"
              "1: Create File",
              "2: Display Students with grade A",
              "3: Exit", sep="\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            create()
        elif choice == "2":
            display()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("INVALID CHOICE TRY AGAIN...")


menu()
