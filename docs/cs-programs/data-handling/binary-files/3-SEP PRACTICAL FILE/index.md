# SCHOOL RESOURCES ARCHIVE

All school related resources stored here.
_(maintained by Sujal Singh)_

### RESOURCE LIST

## <br>Q1) Write a menu driven program to do the following functions:-<br>    a) To create a binary file ‘student.dat’ containing fields as rno, name, marks and grade in a list.<br>    b) Display the details of all those students who have got grade A.<br>
```python
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

```
## <br>2) Write a menu driven program to do the following:-<br>    a) To create a binary file ‘product.dat’ in the following format :<br>       {‘name’ : ‘file’, ‘price’ : 112}, {‘name’ : ‘pen’, ‘price’ : 30}, etc.<br>    b) To display the above file<br>    c) Transfer all the records from binary file ‘product.dat’ to ‘new.dat’ whose price is less than 100.<br>
```python
"""
2) Write a menu driven program to do the following:-
    a) To create a binary file ‘product.dat’ in the following format :
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
        print(f"{item['name']} : ₹{item['price']}")


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
        print(f"{item['name']} : ₹{item['price']}")


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
## <br>Q3) Write a menu driven program to do the following:-<br>    a) To create a binary file ‘student.dat’ containing fields as rno, name, marks and grade in a list.<br>    b) Function to update a record for a given roll number without using another file.<br>    b) Display the file after and before updation<br>
```python
"""
Q3) Write a menu driven program to do the following:-
    a) To create a binary file ‘student.dat’ containing fields as rno, name, marks and grade in a list.
    b) Function to update a record for a given roll number without using another file.
    b) Display the file after and before updation
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

```
## <br>4) Write a menu driven program to do the following:-<br>   a) To create a binary file ‘student.dat’ containing fields as rno, name, marks and grade in a list.<br>   b) Function to delete a record for a given roll number.<br>   b) Display the file after and before updation<br>
```python
"""
4) Write a menu driven program to do the following:-
   a) To create a binary file ‘student.dat’ containing fields as rno, name, marks and grade in a list.
   b) Function to delete a record for a given roll number.
   b) Display the file after and before updation
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

```
## <br>5) Write a menu driven program to do the following:-<br>   a) To create a binary file ‘item.dat’ containing fields as<br>      item_id, item_name, price, quantity in the following format:<br>      [[121,pen,20,5],[21,pencil,10,10],…..]<br>   b) To display the above file<br>   c) Add more item details in the existing file.<br>   d) Display the details of an item for a given item_id.<br>
```python
"""
5) Write a menu driven program to do the following:-
   a) To create a binary file ‘item.dat’ containing fields as
      item_id, item_name, price, quantity in the following format:
      [[121,pen,20,5],[21,pencil,10,10],…..]
   b) To display the above file
   c) Add more item details in the existing file.
   d) Display the details of an item for a given item_id.
"""
import pickle


def create():
    data = []
    while input("Enter values (y/n): ").lower() == "y":
        data.append([
            int(input("Enter item id: ")),
            input("Enter item name: "),
            float(input("Enter item price: ")),
            int(input("Enter item quantity: "))
        ])
    file = open("student.dat", "wb")
    pickle.dump(data, file)
    file.close()


def display():
    file = open("student.dat", "rb")
    data = pickle.load(file)
    file.close()
    for item in data:
        print("ITEM ID: {} | ITEM NAME: {} | PRICE: {} | QUANTITY: {}".format(*item))


def append():
    file = open("student.dat", "rb")
    data = pickle.load(file)
    file.close()
    print("ENTER NEW ITEMS")
    while input("Enter values (y/n): ").lower() == "y":
        data.append([
            int(input("Enter item id: ")),
            input("Enter item name: "),
            float(input("Enter item price: ")),
            int(input("Enter item quantity: "))
        ])

    file = open("student.dat", "wb")
    pickle.dump(data, file)
    file.close()


def seek():
    file = open("student.dat", "rb")
    data = pickle.load(file)
    file.close()
    search_id = int(input("Enter search item id: "))
    for item in data:
        current_id = item[0]
        if current_id == search_id:
            print("ITEM ID: {} | ITEM NAME: {} | PRICE: {} | QUANTITY: {}".format(*item))
            break
    else:
        print("NO MATCH FOUND")


def menu():
    while True:
        print("\n"
              "1: Create File",
              "2: Display File",
              "3: Append to file",
              "4: Search for item",
              "5: Exit", sep="\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            create()
        elif choice == "2":
            display()
        elif choice == "3":
            append()
        elif choice == "4":
            seek()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("INVALID CHOICE TRY AGAIN...")


menu()

```


---

#### [RAISE AN ISSUE](https://github.com/sujaldev/school/issues/new/choose) ON GITHUB IF

- Answer is wrong
- Want a missing question to be added
- Need help with a question
- Need help navigating the website
- Website has a bug

#### WANT TO CONTRIBUTE RESOURCES?

_Fork this [repository](https://github.com/sujaldev/school), make changes, create a pull request._

---

# Comments

<script src="https://giscus.app/client.js"
        data-repo="sujaldev/school"
        data-repo-id="MDEwOlJlcG9zaXRvcnkzODUzMDMzOTI="
        data-category="Q&A"
        data-category-id="DIC_kwDOFvdDYM4CArKZ"
        data-mapping="pathname"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-theme="light"
        data-lang="en"
        crossorigin="anonymous"
        async>
</script>