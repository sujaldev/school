# SCHOOL RESOURCES ARCHIVE

All school related resources stored here.

#### THIS WEBSITE IS MAINTAINED BY SUJAL SINGH

### RESOURCE LIST

##  1)WAP to create a text file of story.txt with one line at a time. Display the file.
```python
# 1)WAP to create a text file of story.txt with one line at a time. Display the file.

def create_file():
    file = open("story.txt", "w")
    while input("Enter values (y/n): ").lower() == "y":
        file.write(input("Enter text: ") + "\n")
    file.close()


create_file()

```
##  2)Write a menu driven program to create a file using writelines() and display the text file using readline() depending on the choice of user.
```python
# 2)Write a menu driven program to create a file using writelines() and display the text file using readline()
# depending on the choice of user.


def create():
    file = open("create_display.txt", "w")
    lines = []
    while input("Enter lines? (y/n): ").lower() == "y":
        lines.append(input("Line to enter: "))
    file.writelines("\n".join(lines))
    file.close()


def display():
    file = open("create_display.txt")
    print("".join(file.readlines()))
    file.close()


def menu():
    while True:
        print("1 = CREATE FILE\n2 = DISPLAY FILE\n3 = EXIT")
        choice = int(input("Enter Choice: "))
        if choice == 1:
            create()
        elif choice == 2:
            display()
        else:
            break


menu()

```
##  3)Write a function to count and display number of words which starts with alphabet a in an existing text file 'story.txt'.
```python
# 3)Write a function to count and display number of words which
# starts with alphabet a in an existing text file 'story.txt'.


def count_a():
    file = open("story.txt")
    count = 0
    for word in file.read().split(" "):
        if word.startswith("a"):
            count += 1
    print(f"There are {count} words which start with a.")
    file.close()


count_a()

```
##  4)WAF to display the number of lines in the file ‘story.txt’.
```python
# 4)WAF to display the number of lines in the file ‘story.txt’.


def count_lines():
    file = open("story.txt")
    print(f"There are {len(file.readlines())} lines in the file story.txt")
    file.close()


count_lines()

```
##  5)WAF to display the number of characters of file ‘first.txt’ without counting EOL characters.
```python
# 5)WAF to display the number of characters of file ‘first.txt’ without counting EOL characters.

def count_char():
    file = open("first.txt")
    char_count = len(file.read().replace("\n", ""))
    print(f"There are {char_count} characters in the file first.txt")
    file.close()


count_char()

```
##  6)WAF to count and display number of words in each line of text file "first.txt".
```python
# 6)WAF to count and display number of words in each line of text file "first.txt".

def count_words():
    file = open("first.txt")
    i = 1
    for line in file.readlines():
        print(f"{len(line)} words at line no {i}")
        i += 1
    file.close()


count_words()

```
##  7)WAF to read a text file and display the count of vowels and consonants in the file ‘poem.txt’.
```python
# 7)WAF to read a text file and display the count of vowels and consonants in the file ‘poem.txt’.

def grammar():
    file = open("poem.txt")
    data = file.read().replace("\n", "").replace(" ", "")
    l = ["v" if char.lower() in "aeiou" else "c" for char in data]
    vowel_count, const_count = l.count("v"), l.count("c")
    print(f"Vowel Count = {vowel_count} and Consonant Count = {const_count}")
    file.close()


grammar()

```
##  8)WAF to display the size of a file after removing EOL characters, leading and trailing spaces and blank lines.
```python
# 8)WAF to display the size of a file after removing EOL characters, leading and trailing spaces and blank lines.


def count_and_display():
    file = open("poem.txt")
    output = []
    for line in file.readlines():
        output.append(line.strip().replace('\n', ''))
    print(len("".join(output)), "Bytes")
    file.close()


count_and_display()

```
##  9)WAF to reverse and display each line of text from a already created text file ‘poem.txt’.
```python
# 9)WAF to reverse and display each line of text from a already created text file ‘poem.txt’.

def reverse():
    file = open("poem.txt")
    for line in file.readlines():
        print(line[::-1])
    file.close()


reverse()

```
##  10)WAF to find and display the occurrence of the word ‘we’ in text file ‘poem.txt’.
```python
# 10)WAF to find and display the occurrence of the word ‘we’ in text file ‘poem.txt’.

def we_count():
    file = open("poem.txt")
    count = file.read().replace("\n", " ").split(" ").count("we")
    print(f"There are {count} occurrences of the word we in poem.txt")
    file.close()


we_count()

```
##  11)WAF to read the text from file ‘poem.txt’ and replace the occurrence of ‘that’ with ‘this’ and store the entire file content after replacement in file ‘ufile.txt’.
```python
# 11)WAF to read the text from file ‘poem.txt’ and
# replace the occurrence of ‘that’ with ‘this’ and
# store the entire file content after replacement in file ‘ufile.txt’.

def replace_that():
    file, new_file = open("poem.txt"), open("ufile.txt", "w")
    new_file.write(file.read().replace("that", "this"))
    file.close()
    new_file.close()


replace_that()

```
##  12)WAF to count and display the words ending with ‘e’ in a text file ‘poem.txt’.
```python
# 12)WAF to count and display the words ending with ‘e’ in a text file ‘poem.txt’.

def count_e():
    file = open("poem.txt")
    count = 0
    for word in file.read().replace("\n", " ").split(" "):
        if word.endswith("e"):
            count += 1
    print(f"{count} words in poem.txt end with e")
    file.close()


count_e()

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