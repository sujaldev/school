# SCHOOL RESOURCES ARCHIVE

All school related resources stored here.
_(maintained by Sujal Singh)_

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
## <br>Q3)[PRACTICAL] Write a menu driven program to do the following:-<br>   a) To create a binary file 'product.dat' in the following format :<br>    {‘name’ : ‘file’, ‘price’ : 113}, {‘name’ : ‘pen’, ‘price’ : 30}, etc.<br>   b) To display the above file<br>   c) Transfer all the records from binary file ‘product.dat’ to ‘new.dat’ whose price is less than 101.<br>
```python
"""
Q3)[PRACTICAL] Write a menu driven program to do the following:-
   a) To create a binary file 'product.dat' in the following format :
    {‘name’ : ‘file’, ‘price’ : 113}, {‘name’ : ‘pen’, ‘price’ : 30}, etc.
   b) To display the above file
   c) Transfer all the records from binary file ‘product.dat’ to ‘new.dat’ whose price is less than 101.
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
## <br>4)[PRACTICAL] Write a menu driven program to do the following:-<br>   a) To create a binary file 'student.dat' containing fields as rno, name, marks and grade in a list.<br>   b) Function to update a record for a given roll number without using another file.<br>   b) Display the file after and before updating<br>
```python
"""
4)[PRACTICAL] Write a menu driven program to do the following:-
   a) To create a binary file 'student.dat' containing fields as rno, name, marks and grade in a list.
   b) Function to update a record for a given roll number without using another file.
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


def update():
    db = read()
    file = open("student.dat", "wb")
    old_no, new_no = int(input("Enter roll no to look for: ")), int(input("Enter new roll no: "))
    new_name, new_grade = input("Enter updated name: "), input("Enter updated grade: ")
    matched = False

    for student in db:
        print("OLD: ", f"{student[1]} with roll number {student[0]} has grade {student[2]}")
        if student[0] == old_no:
            student[0], matched = new_no, True
            student[1], student[2] = new_name, new_grade
        print("NEW: ", f"{student[1]} with roll number {student[0]} has grade {student[2]}")
        pickle.dump(student, file)
    file.close()

    if not matched:
        print("NO MATCH FOUND, NOT UPDATED")


def menu():
    while True:
        print("\n"
              "1: Create File",
              "2: Update File",
              "3: Exit", sep="\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            create()
        elif choice == "2":
            update()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("INVALID CHOICE TRY AGAIN...")


menu()

```
## <br>5) [PRACTICAL] Write a menu driven program to do the following:-<br>   a) To create a binary file 'student.dat' containing fields as rno, name, marks and grade in a list.<br>   b) Function to delete a record for a given roll number.<br>   b) Display the file after and before updating<br>
```python
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
            matched = True
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

```
## <br>Q6) [PRACTICAL] Write a menu driven program to do the following:-<br>   a) To create a binary file 'item.dat' containing fields as<br>      item_id, item_name, price, quantity in the following format : [[121,pen,20,5],[21,pencil,10,10],.....]<br>   b) To display the above file<br>   c) Add more item details in the existing file.<br>   d) Display the details of an item for a given item_id.<br>
```python
"""
Q6) [PRACTICAL] Write a menu driven program to do the following:-
   a) To create a binary file 'item.dat' containing fields as
      item_id, item_name, price, quantity in the following format : [[121,pen,20,5],[21,pencil,10,10],.....]
   b) To display the above file
   c) Add more item details in the existing file.
   d) Display the details of an item for a given item_id.
"""
import pickle


def create():
    wrapper = []
    while input("Enter values (y/n): ").lower() == "y":
        wrapper.append([
            int(input("Enter ITEM ID: ")),
            input("Enter ITEM NAME: "),
            float(input("Enter ITEM PRICE: ")),
            int(input("Enter quantity: "))
        ])
    file = open("item.dat", "wb")
    pickle.dump(wrapper, file)
    file.close()


def display():
    try:
        file = open("item.dat", "rb")
        for entry in pickle.load(file):
            print(f"\nITEM ID: {entry[0]}",
                  f"ITEM NAME: {entry[1]}",
                  f"ITEM PRICE: {entry[2]}",
                  f"ITEM QUANTITY: {entry[3]}\n", sep="\n")
    except FileNotFoundError:
        print("\nFILE DOES NOT EXIST YET! CREATE FILE FIRST\n")


def item_append():
    try:
        file = open("item.dat", "rb")
        data = pickle.load(file)
        file.close()

        while input("Enter values (y/n):").lower() == "y":
            data.append([
                int(input("Enter ITEM ID:")),
                input("Enter ITEM NAME:"),
                float(input("Enter ITEM PRICE:")),
                int(input("Enter ITEM QUANTITY:"))
            ])

        file = open("item.dat", "wb")
        pickle.dump(data, file)
        file.close()
    except FileNotFoundError:
        print("\nFILE DOES NOT EXIST YET! CREATE THE FILE FIRST\n")


def lookup():
    try:
        file = open("item.dat", "rb")
        item_id = int(input("Enter ITEM ID to look for: "))
        match = []
        for entry in pickle.load(file):
            if item_id == entry[0]:
                match = entry
                break
        file.close()

        if match:
            print(f"\nITEM ID: {match[0]}",
                  f"ITEM NAME: {match[1]}",
                  f"ITEM PRICE: {match[2]}",
                  f"ITEM QUANTITY: {match[3]}\n", sep="\n")
        else:
            print("\nMATCH NOT FOUND\n")
    except FileNotFoundError:
        print("\nFILE DOES NOT EXIST YET! CREATE THE FILE FIRST\n")


def menu():
    while True:
        print("1: CREATE FILE",
              "2: DISPLAY FILE",
              "3: ADD MORE ITEMS",
              "4: LOOKUP ITEM",
              "5: EXIT", sep="\n")

        choice = input("ENTER CHOICE: ")

        if choice == "1":
            create()
        elif choice == "2":
            display()
        elif choice == "3":
            item_append()
        elif choice == "4":
            lookup()
        elif choice == "5":
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