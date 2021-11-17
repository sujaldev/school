# SCHOOL RESOURCES ARCHIVE

All school related resources stored here.

#### THIS WEBSITE IS MAINTAINED BY SUJAL SINGH

### RESOURCE LIST

## <br>Q1) A blood bank maintains a binary file that contains following information for every donor: name,<br>date of birth, address, phone number and blood group. Write a program in Python to do the following<br>(using user defined functions):<br>    a) Create the file of donors [donor.dat]<br>    b) Display the records.<br>    c) For Input of a specific blood group, display the name and address of donors of<br>     that blood group.<br>
```python
"""
Q1) A blood bank maintains a binary file that contains following information for every donor: name,
date of birth, address, phone number and blood group. Write a program in Python to do the following
(using user defined functions):
    a) Create the file of donors [donor.dat]
    b) Display the records.
    c) For Input of a specific blood group, display the name and address of donors of
     that blood group.
"""
import pickle


def create():
    # COLLECT USER INPUT
    data = []
    while input("Enter values (y/n): ").lower() == "y":
        data.append([
            input("Enter donor name: "),
            input("Enter DOB (dd/mm/yyyy): "),
            input("Enter address: "),
            input("Enter phone number: "),
            input("Enter blood group: ")
        ])

    # (CREATE AND) WRITE TO BINARY FILE
    with open("donor.dat", "wb") as db:
        pickle.dump(data, db)


def display():
    with open("donor.dat", "rb") as db:
        data = pickle.load(db)

    template = "| {:^20} || {:^20} || {:^20} || {:^20} || {:^20} |"
    for donor in data:
        print(template.format(*donor))


def seek():
    with open("donor.dat", "rb") as db:
        data = pickle.load(db)

    wanted_group = input("Enter the desired blood group: ")
    for donor in data:
        if donor[-1] == wanted_group:
            print(
                f"Name: {donor[0]}",
                f"Address: {donor[2]}\n", sep="\n"
            )


def menu():
    while True:
        choice = input(
            "\n\n"
            "1. Create donor database\n"
            "2. Display donor records\n"
            "3. Find Donor by blood group\n"
            "4. Exit\n"
            "Enter your choice: "
        )

        if choice == "1":
            create()
        elif choice == "2":
            display()
        elif choice == "3":
            seek()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice... Try again...")


menu()

```
## <br>Q2) A school maintains a binary file that contains following information for every student: roll<br>number, name, marks and grade. Write a program in Python to do the following (using user defined<br>functions):<br>    a) Create the file of students [student.dat]<br>    b) Display the records of all ‘A’ grade students.<br>
```python
"""
Q2) A school maintains a binary file that contains following information for every student: roll
number, name, marks and grade. Write a program in Python to do the following (using user defined
functions):
    a) Create the file of students [student.dat]
    b) Display the records of all ‘A’ grade students.
"""
```
## <br>Q3) Write program in Python to do the following (using user defined functions):<br>    a) Create a CSV file containing word and its meaning.<br>    b) Determine the meaning for the given word.<br>    c) To display all word and meanings<br>
```python
"""
Q3) Write program in Python to do the following (using user defined functions):
    a) Create a CSV file containing word and its meaning.
    b) Determine the meaning for the given word.
    c) To display all word and meanings
"""
```
## <br>Q4) Write a menu driven program in Python to do the following(using user defined functions) :<br>    a) to create a text file “MYFILE.TXT” and store strings in it .<br>    b) display all strings of the text file.<br>    c) to count the number of words starting with ‘A’ .<br>
```python
"""
Q4) Write a menu driven program in Python to do the following(using user defined functions) :
    a) to create a text file “MYFILE.TXT” and store strings in it .
    b) display all strings of the text file.
    c) to count the number of words starting with ‘A’ .
"""
```
## <br>Q5) Write a menu driven program in Python to do the following using user defined functions:<br>    a) to create a text file “DIARY.TXT” and store strings in it .<br>    b) display all strings of the text file.<br>    c) to count the no. of “Me” or “My” words present in a text file “DIARY.TXT”.<br>If the file “DIARY.TXT” content is as follows :<br>My first book was Me and My family. It gave me a chance to be known to the world.<br>The output of the function should be<br>Count of Me/My in file : 4<br>
```python
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
```


---

### [RAISE AN ISSUE](https://github.com/sujaldev/school/issues/new/choose) ON GITHUB IF

- Answer is wrong
- Want a missing question to be added
- Need help with a question
- Need help navigating the website
- Website has a bug

### WANT TO CONTRIBUTE RESOURCES?

Fork my [repository](https://github.com/sujaldev/school) \
After adding changes, create a pull request.