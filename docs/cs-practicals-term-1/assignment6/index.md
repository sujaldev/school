# SCHOOL RESOURCES ARCHIVE

All school related resources stored here.
_(maintained by Sujal Singh)_

### RESOURCE LIST

## <br>A menu driven program to do the following:<br>    a) Display the file 'story.txt'.<br>    b) Count and display all the words which starts with alphabet 'a' or 'A' from an existing file<br>       'story.txt' using read function.<br>
```python
"""
A menu driven program to do the following:
    a) Display the file 'story.txt'.
    b) Count and display all the words which starts with alphabet 'a' or 'A' from an existing file
       'story.txt' using read function.
"""


def display():
    try:
        story = open("story.txt")
        print(story.read(), end="\n\n")
        story.close()
    except FileNotFoundError:
        print("No such file exists...")


def count_display():
    try:
        story = open("story.txt")
        words = story.read().replace("\n", " ").split(" ")
        words = [w for w in words if w[0].lower() == "a"]
        print(f"{len(words)} words start with 'a' or 'A':")
        print("\n".join(words), end="\n\n")
        story.close()
    except FileNotFoundError:
        print("No such file exits...")


def menu():
    while True:
        print("\n1. Display story.txt",
              "2. Count and display words starting with a or A",
              "3. Exit", sep="\n")
        choice = input("Enter choice: ")

        if choice == "1":
            display()
        elif choice == "2":
            count_display()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again...")


menu()

"""
OUTPUT:
1. Display story.txt
2. Count and display words starting with a or A
3. Exit
Enter choice: 1
Hello astronaut
Ola Amigos!
this is a line that ends with an A
on the other hand this ends with an a


1. Display story.txt
2. Count and display words starting with a or A
3. Exit
Enter choice: 2
7 words start with 'a' or 'A':
astronaut
Amigos!
a
an
A
an
a


1. Display story.txt
2. Count and display words starting with a or A
3. Exit
Enter choice: 3
Exiting...
"""

```
## <br>Write a menu driven program to do the following:<br>    a) Display the file 'story.txt'.<br>    b) Count and display all the lines which ends with alphabet 'a' or 'A' use readlines function to<br>    read the content.<br>
```python
"""
Write a menu driven program to do the following:
    a) Display the file 'story.txt'.
    b) Count and display all the lines which ends with alphabet 'a' or 'A' use readlines function to
    read the content.
"""


def display():
    try:
        story = open("story.txt")
        print(story.read(), end="\n\n")
        story.close()
    except FileNotFoundError:
        print("No such file exists...")


def count_display():
    try:
        story = open("story.txt")
        lines = [l for l in story.readlines() if l.replace("\n", "")[-1].lower() == "a"]
        print(f"{len(lines)} lines end with 'a' or 'A':")
        print("".join(lines), end="\n\n")
        story.close()
    except FileNotFoundError:
        print("No such file exists...")


def menu():
    while True:
        print("1. Display story.txt",
              "2. Count and display lines that end with 'a' or 'A'",
              "3. Exit", sep="\n")
        choice = input("Enter choice: ")

        if choice == "1":
            display()
        elif choice == "2":
            count_display()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again\n")


menu()

"""
OUTPUT:
1. Display story.txt
2. Count and display lines that end with 'a' or 'A'
3. Exit
Enter choice: 1
Hello astronaut
Ola Amigos!
this is a line that ends with an A
on the other hand this ends with an a

1. Display story.txt
2. Count and display lines that end with 'a' or 'A'
3. Exit
Enter choice: 2
2 lines end with 'a' or 'A':
this is a line that ends with an A
on the other hand this ends with an a

1. Display story.txt
2. Count and display lines that end with 'a' or 'A'
3. Exit
Enter choice: 3
Exiting...
"""

```
## <br>Write a menu driven program to do the following:<br>    a) Add more lines(one at a time) in an existing file 'story.txt'.<br>    b) Display the content of the file using readline function.<br>
```python
"""
Write a menu driven program to do the following:
    a) Add more lines(one at a time) in an existing file 'story.txt'.
    b) Display the content of the file using readline function.
"""


def append_lines():
    story = open("story.txt", "a")
    while input("Enter lines (y/n): ").lower() == "y":
        story.write("\n" + input("Enter line: "))
    story.close()


def display():
    try:
        story = open("story.txt")
        line = story.readline()
        while line:
            print(line, end="")
            line = story.readline()
        print("\n")
        story.close()
    except FileNotFoundError:
        print("No such file exits...")


def menu():
    while True:
        print("1. Append lines to 'story.txt'",
              "2. Display 'story.txt' line by line",
              "3. Exit", sep="\n")
        choice = input("Enter choice: ")

        if choice == "1":
            append_lines()
        elif choice == "2":
            display()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again...")


menu()

"""
OUTPUT:
1. Append lines to 'story.txt'
2. Display 'story.txt' line by line
3. Exit
Enter choice: 1
Enter lines (y/n): y
Enter line: this is appended line 1
Enter lines (y/n): y
Enter line: this is appended line 2
Enter lines (y/n): n
1. Append lines to 'story.txt'
2. Display 'story.txt' line by line
3. Exit
Enter choice: 2
Hello astronaut
Ola Amigos!
this is a line that ends with an A
on the other hand this ends with an a
this is appended line 1
this is appended line 2

1. Append lines to 'story.txt'
2. Display 'story.txt' line by line
3. Exit
Enter choice: 3
Exiting...
"""

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