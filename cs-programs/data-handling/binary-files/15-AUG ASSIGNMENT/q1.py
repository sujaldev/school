# Q1) WAF to create a binary file 'student.dat' storing the student details as
# roll number, name and the marks depending on the choice of the user.
import pickle


def create():
    file = open("student.dat", "wb")
    while input("Enter values (y/n): ").lower() == "y":
        print()
        pickle.dump([
            int(input("Enter roll number: ")),
            input("Enter student's name: "),
            float(input("Enter student's marks: "))
        ], file)
    file.close()


create()
