# SCHOOL RESOURCES ARCHIVE

All school related resources stored here.
#### THIS WEBSITE IS MAINTAINED BY SUJAL SINGH

### RESOURCE LIST

##  Q1) WAF to create a binary file 'student.dat' storing the student details as roll number, name and the marks depending on the choice of the user.
```python
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

```
## <br>2) [PRACTICAL] Write a menu driven program to do the following functions:-<br>a) To create a binary file 'student.dat' containing fields as rno, name, marks and grade in a list.<br>b) Display the details of all those students who have got grade A.<br>
```python
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

```
## <br>Q3)[PRACTICAL] Write a menu driven program to do the following:-<br>   a) To create a binary file 'product.dat' in the following format :<br>    {‘name’ : ‘file’, ‘price’ : 112}, {‘name’ : ‘pen’, ‘price’ : 30}, etc.<br>   b) To display the above file<br>   c) Transfer all the records from binary file ‘product.dat’ to ‘new.dat’ whose price is less than 100.<br>
```python
"""
Q3)[PRACTICAL] Write a menu driven program to do the following:-
   a) To create a binary file 'product.dat' in the following format :
    {‘name’ : ‘file’, ‘price’ : 112}, {‘name’ : ‘pen’, ‘price’ : 30}, etc.
   b) To display the above file
   c) Transfer all the records from binary file ‘product.dat’ to ‘new.dat’ whose price is less than 100.
"""
import pickle


def create():
    file = open("product.dat", "wb")
    while input("Enter values (y/n): ").lower() == "y":
        print()
        pickle.dump({
            "name": input("Enter product name: "),
            "price": float(input("Enter price: "))
        }, file)
    file.close()


def read(file_name):
    try:
        file = open(file_name, "rb")
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


def display():
    db = read("product.dat")
    for item in db:
        print(f"cost of 1 {item['name']} is {item['price']}")


def transfer():
    new_file = open("new.dat", "wb")
    db = read("product.dat")
    for item in db:
        if item["price"] < 100:
            pickle.dump(item, new_file)
    new_file.close()


def display_transferred():
    db = read("new.dat")
    for item in db:
        print(f"cost of 1 {item['name']} is {item['price']}")


def menu():
    while True:
        print("\n"
              "1: Create File",
              "2: Display File",
              "3: Transfer Cheap",
              "4: Display New File",
              "5: Exit", sep="\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            create()
        elif choice == "2":
            display()
        elif choice == "3":
            transfer()
        elif choice == "4":
            display_transferred()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("INVALID CHOICE TRY AGAIN...")


menu()

```


### ENCOUNTERED SOMETHING WRONG?
Raise an issue on [github](https://github.com/sujaldev/school) to report anything.