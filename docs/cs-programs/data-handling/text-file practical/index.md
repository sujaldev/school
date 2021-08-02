# SCHOOL RESOURCES ARCHIVE

All school related resources stored here.

### RESOURCES

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


display()
count()

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
    file = open("story.txt")
    data = file.read().replace("\n", " ").split(" ")
    print("WORDS ENDING WITH A")
    w_count = 0
    for word in data:
        if word[-1].lower() in "aA":
            print(word)
            w_count += 1
    print("COUNT:", w_count)


display()
count()

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


append_lines()
display_by_line()

```


### Other
Raise an issue on [github](https://github.com/sujaldev/school) to report anything.