# SCHOOL RESOURCES ARCHIVE

All school related resources stored here.

#### THIS WEBSITE IS MAINTAINED BY SUJAL SINGH

### RESOURCE LIST

## <br>WAP to store name and total marks in a dictionary by taking input from user and then find<br>Topper or Toppers by copying their records in other dictionary.<br>
```python
"""
WAP to store name and total marks in a dictionary by taking input from user and then find
Topper or Toppers by copying their records in other dictionary.
"""
student_data, topper_data = {}, {}
table_spacing = 20

while input("Enter records (y/n): ").lower() == "y":
    name, marks = input("Enter student name: "), float(input("Enter student marks: "))
    student_data[name] = marks

print("\nToppers:")
print("Name".center(20), "Marks".center(20), sep="|")
print("_" * 42)
for name, marks in student_data.items():
    if marks >= 90:
        print(name.center(20), str(marks).center(20), sep="|")
        topper_data[name] = marks

"""
OUTPUT:
Enter records (y/n): y
Enter student name: feynman
Enter student marks: 99
Enter records (y/n): y
Enter student name: turing
Enter student marks: 85
Enter records (y/n): n

Toppers:
        Name        |       Marks        
__________________________________________
      feynman       |        99.0       
"""

```
## <br>Write a menu driven Program to Store Name and Phone number in a dictionary, Input Name<br>and search his/her phone number, Input Phone and search its owner name. Traverse the<br>whole dictionary depending on choice of the user.<br>
```python
"""
Write a menu driven Program to Store Name and Phone number in a dictionary, Input Name
and search his/her phone number, Input Phone and search its owner name. Traverse the
whole dictionary depending on choice of the user.
"""
phonebook = {}

while True:
    print("1. Create phonebook",
          "2. Search phone number by name",
          "3. Search name by phone number",
          "4. Exit", sep="\n")
    choice = input("Enter choice: ")

    if choice == "1":
        while input("Enter values (y/n): ").lower() == "y":
            name, number = input("Enter name: "), input("Enter number: ")
            if name not in phonebook.keys():
                phonebook[name] = number
            else:
                print("This name already exists, try again")

    elif choice == "2":
        name = input("Enter name to look for: ")
        if name in phonebook.keys():
            print(f"{name} owns the number {phonebook[name]}")
        else:
            print("No such person exists in record.")

    elif choice == "3":
        number = input("Enter number to look for: ")
        for name, phone in phonebook.items():
            if phone == number:
                print(f"The number {number} belongs to {name}.")
                break
        else:
            print("No such number exists in record.")

    elif choice == "4":
        print("exiting...")
        break

    else:
        print("Invalid choice.")

"""
OUTPUT:
1. Create phonebook
2. Search phone number by name
3. Search name by phone number
4. Exit
Enter choice: 1
Enter values (y/n): y
Enter name: feynman
Enter number: 1234
Enter values (y/n): y
Enter name: turing
Enter number: 4321
Enter values (y/n): n
1. Create phonebook
2. Search phone number by name
3. Search name by phone number
4. Exit
Enter choice: 2
Enter name to look for: turing
turing owns the number 4321
1. Create phonebook
2. Search phone number by name
3. Search name by phone number
4. Exit
Enter choice: 2
Enter name to look for: john
No such person exists in record.
1. Create phonebook
2. Search phone number by name
3. Search name by phone number
4. Exit
Enter choice: 3
Enter number to look for: 1234
The number 1234 belongs to feynman.
1. Create phonebook
2. Search phone number by name
3. Search name by phone number
4. Exit
Enter choice: 3
Enter number to look for: 987967
No such number exists in record.
1. Create phonebook
2. Search phone number by name
3. Search name by phone number
4. Exit
Enter choice: 4
exiting...
"""
```
## <br>Write a Python program to create a dictionary of students where name is the key, marks is<br>the value of the dictionary. Create another dictionary from existing one after removing keys<br>containing duplicate values from the Dictionary.<br>
```python
"""
Write a Python program to create a dictionary of students where name is the key, marks is
the value of the dictionary. Create another dictionary from existing one after removing keys
containing duplicate values from the Dictionary.
"""
db = {}
print("Create student database:")
while input("Enter record (y/n): ").lower() == "y":
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    db[name] = marks

unique_values, unique_dict = [], {}
for key, val in db.items():
    if val not in unique_values:
        unique_values.append(val)
        unique_dict[key] = val

print("Unique entries:")
for name, marks in unique_dict.items():
    print(f"{name}: {marks}")

"""
OUTPUT:
Create student database:
Enter record (y/n): y
Enter name: feynman
Enter marks: 99
Enter record (y/n): y
Enter name: turing
Enter marks: 99
Enter record (y/n): y
Enter name: neumann
Enter marks: 85
Enter record (y/n): n
Unique entries:
feynman: 99.0
neumann: 85.0
"""

```
## <br>WAP to create a dictionary of n employees where names are keys and values of each<br>employee is a collection of BASIC(input by the user), DA(20% of Basic), HRA(10% of Basic),<br>TA(10% of Basic). Calculate and display the total salary of each employee.<br>
```python
"""
WAP to create a dictionary of n employees where names are keys and values of each
employee is a collection of BASIC(input by the user), DA(20% of Basic), HRA(10% of Basic),
TA(10% of Basic). Calculate and display the total salary of each employee.
"""
while input("Enter more employees (y/n): ").lower() == "y":
    basic = int(input("Enter basic: "))
    da = 0.2 * basic
    hra = ta = 0.1 * basic
    print("Total salary:", basic + da + hra + ta)

"""
OUTPUT:
Enter more employees (y/n): y
Enter basic: 200
Total salary: 280.0
Enter more employees (y/n): y
Enter basic: 300
Total salary: 420.0
Enter more employees (y/n): n
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