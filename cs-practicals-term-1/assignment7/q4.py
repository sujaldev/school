"""
Write a menu driven program to do the following:-
   a) To create a binary file ‘student.dat’ containing fields as rno, name, marks and grade in a list.
   b) Function to delete a record for a given roll number.
   b) Display the file after and before updating
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
    try:
        while True:
            student = pickle.load(file)
            print("Roll No: {} | Student Name: {} | Marks: {} | Grades: {}".format(*student))
    except EOFError:
        file.close()


def delete():
    print("FILE BEFORE DELETION:")
    display()

    file = open("student.dat", "rb")
    search_roll_no, matched = int(input("Enter roll no to look for: ")), False
    buffer = []
    try:
        while True:
            student_data = pickle.load(file)
            current_roll_no = student_data[0]
            if current_roll_no != search_roll_no:
                buffer.append(student_data)
            else:
                matched = True
    except EOFError:
        file.close()

    if not matched:
        print("NO MATCH WAS FOUND")
    else:
        file = open("student.dat", "wb")
        for student in buffer:
            pickle.dump(student, file)
        file.close()
        print("DELETED SUCCESSFULLY, NEW FILE:")
        display()


def menu():
    while True:
        print("\n"
              "1: Create File",
              "2: Display File",
              "3: Delete Student and Display",
              "4: Exit", sep="\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            create()
        elif choice == "2":
            display()
        elif choice == "3":
            delete()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("INVALID CHOICE TRY AGAIN...")


menu()

"""
OUTPUT:
1: Create File
2: Display File
3: Delete Student and Display
4: Exit
Enter your choice: 1
Add values (y/n): y
Enter roll no: 1
Enter student name: feynman
Enter student's marks: 99
Enter student's grade: A
Add values (y/n): y
Enter roll no: 2
Enter student name: turing
Enter student's marks: 95
Enter student's grade: A
Add values (y/n): n

1: Create File
2: Display File
3: Delete Student and Display
4: Exit
Enter your choice: 2
Roll No: 1 | Student Name: feynman | Marks: 99 | Grades: A
Roll No: 2 | Student Name: turing | Marks: 95 | Grades: A

1: Create File
2: Display File
3: Delete Student and Display
4: Exit
Enter your choice: 3
FILE BEFORE DELETION:
Roll No: 1 | Student Name: feynman | Marks: 99 | Grades: A
Roll No: 2 | Student Name: turing | Marks: 95 | Grades: A
Enter roll no to look for: 2
DELETED SUCCESSFULLY, NEW FILE:
Roll No: 1 | Student Name: feynman | Marks: 99 | Grades: A

1: Create File
2: Display File
3: Delete Student and Display
4: Exit
Enter your choice: 3
FILE BEFORE DELETION:
Roll No: 1 | Student Name: feynman | Marks: 99 | Grades: A
Enter roll no to look for: 899
NO MATCH WAS FOUND

1: Create File
2: Display File
3: Delete Student and Display
4: Exit
Enter your choice: 2
Roll No: 1 | Student Name: feynman | Marks: 99 | Grades: A

1: Create File
2: Display File
3: Delete Student and Display
4: Exit
Enter your choice: 4
Exiting...
"""
