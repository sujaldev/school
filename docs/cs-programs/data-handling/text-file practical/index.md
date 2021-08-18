# SCHOOL RESOURCES ARCHIVE

All school related resources stored here.

#### THIS WEBSITE IS MAINTAINED BY SUJAL SINGH

### RESOURCE LIST

## <br>Q1.WA menu driven program to do the following :<br>(a)	Display the file story.txt<br>(b)	Count and display all those words which starts with alphabet a/A<br>
```python
"""
Q1.WA menu driven program to do the following :
(a)	Display the file story.txt
(b)	Count and display all those words which starts with alphabet a/A
"""


def display():
    file = open("story.txt")
    print("FILE DATA START:\n", file.read(), "\nFILE END\n", sep="")
    file.close()


def count():
    file = open("story.txt")
    data = file.read().replace("\n", " ").split(" ")
    print("WORDS STARTING WITH A:")
    w_count = 0
    for word in data:
        if word[0].lower() in "aA":
            print(word)
            w_count += 1
    print("COUNT:", w_count)


def menu():
    while True:
        print("1: DISPLAY FILE",
              "2: COUNT WORDS STARTING WITH 'A'",
              "3: EXIT", sep="\n")
        choice = input("Enter choice: ")
        if choice == "1":
            display()
        elif choice == "2":
            count()
        elif choice == "3":
            break
        else:
            print("INVALID CHOICE TRY AGAIN")


menu()

```
## <br>Q2. WA menu driven program to do the following :<br>(a)	Display the file story.txt<br>(b)	Count and display all the lines which ends with alphabet a/A<br>
```python
"""
Q2. WA menu driven program to do the following :
(a)	Display the file story.txt
(b)	Count and display all the lines which ends with alphabet a/A
"""


def display():
    file = open("story.txt")
    print("FILE DATA START:\n", file.read(), "\nFILE END\n", sep="")
    file.close()


def count():
    print("LINES ENDING WITH A")
    file = open("story.txt")
    lines = file.readlines()
    w_count = 0
    for line in lines:
        if line[-1].lower() in "aA":
            print(line)
            w_count += 1
    print("COUNT:", w_count)


def menu():
    while True:
        print("1: DISPLAY FILE",
              "2: COUNT LINES ENDING WITH 'A'",
              "3: EXIT", sep="\n")
        choice = input("Enter choice: ")
        if choice == "1":
            display()
        elif choice == "2":
            count()
        elif choice == "3":
            break
        else:
            print("INVALID CHOICE TRY AGAIN")


menu()

```
## <br>Q3. WA menu driven program to do the following :<br>(a)	Add more lines(one at a time) in an existing file story.txt<br>(b)	Display the content of the file using readline()<br>
```python
"""
Q3. WA menu driven program to do the following :
(a)	Add more lines(one at a time) in an existing file story.txt
(b)	Display the content of the file using readline()
"""


def append_lines():
    file = open("story.txt", "a")
    while True:
        line = "\n" + input("Enter line to append: ")
        file.write(line)
        if input("Continue (y/n): ").lower() != "y":
            break


def display_by_line():
    print("FILE START:")
    file = open("story.txt")
    while True:
        line = file.readline()
        print(line, end="")
        if not line:
            break
    file.close()
    print("\nFILE END")


def menu():
    while True:
        print("1: APPEND LINES TO EXISTING FILE",
              "2: DISPLAY FILE USING READLINE",
              "3: EXIT", sep="\n")
        choice = input("Enter choice: ")
        if choice == "1":
            append_lines()
        elif choice == "2":
            display_by_line()
        elif choice == "3":
            break
        else:
            print("INVALID CHOICE TRY AGAIN")


menu()

```


---

### [RAISE AN ISSUE](https://github.com/sujaldev/school/issues/new/choose) ON GITHUB IF

- Answer is wrong
- Need help with a question
- Need help navigating the website
- Website has a bug

### WANT TO CONTRIBUTE RESOURCES?

Fork my [repository](https://github.com/sujaldev/school) \
After adding changes, create a pull request.