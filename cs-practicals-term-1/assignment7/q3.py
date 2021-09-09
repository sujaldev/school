"""
Write a menu driven program to do the following:-
    a) To create a binary file ‘student.dat’ containing fields as rno, name, marks and grade in a list.
    b) Function to update a record for a given roll number without using another file.
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


def update():
    print("FILE BEFORE UPDATING:")
    display()

    file = open("student.dat", "rb")
    search_roll_no, matched = int(input("Enter roll to look for: ")), False
    buffer = []
    try:
        while True:
            student_data = pickle.load(file)
            current_roll_no = student_data[0]
            if current_roll_no == search_roll_no:
                matched = True
                print("MATCH FOUND, UPDATE NOW:")
                buffer.append([
                    int(input("Enter new roll no: ")),
                    input("Enter student new name: "),
                    int(input("Enter student's new marks: ")),
                    input("Enter student's new grade: ")
                ])
            else:
                buffer.append(student_data)
    except EOFError:
        file.close()

    if not matched:
        print("NO MATCH WAS FOUND")

    file = open("student.dat", "wb")
    for student in buffer:
        pickle.dump(student, file)
    file.close()

    print("FILE AFTER UPDATING")
    display()


def menu():
    while True:
        print("\n"
              "1: Create File",
              "2: Display File",
              "3: Update and Display",
              "4: Exit", sep="\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            create()
        elif choice == "2":
            display()
        elif choice == "3":
            update()
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
3: Update and Display
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
Add values (y/n): y
Enter roll no: 3
Enter student name: neumann
Enter student's marks: 80
Enter student's grade: B
Add values (y/n): n

1: Create File
2: Display File
3: Update and Display
4: Exit
Enter your choice: 2
Roll No: 1 | Student Name: feynman | Marks: 99 | Grades: A
Roll No: 2 | Student Name: turing | Marks: 95 | Grades: A
Roll No: 3 | Student Name: neumann | Marks: 80 | Grades: B

1: Create File
2: Display File
3: Update and Display
4: Exit
Enter your choice: 3
FILE BEFORE UPDATING:
Roll No: 1 | Student Name: feynman | Marks: 99 | Grades: A
Roll No: 2 | Student Name: turing | Marks: 95 | Grades: A
Roll No: 3 | Student Name: neumann | Marks: 80 | Grades: B
Enter roll to look for: 2
MATCH FOUND, UPDATE NOW:
Enter new roll no: 4
Enter student new name: alan
Enter student's new marks: 90
Enter student's new grade: A
FILE AFTER UPDATING
Roll No: 1 | Student Name: feynman | Marks: 99 | Grades: A
Roll No: 4 | Student Name: alan | Marks: 90 | Grades: A
Roll No: 3 | Student Name: neumann | Marks: 80 | Grades: B

1: Create File
2: Display File
3: Update and Display
4: Exit
Enter your choice: 4
Exiting...
"""
