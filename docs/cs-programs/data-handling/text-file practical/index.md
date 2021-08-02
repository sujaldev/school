# SCHOOL RESOURCES ARCHIVE

All school related resources stored here.

### RESOURCES

## 
Q1.WA menu driven program to do the following :
(a)	Display the file story.txt
(b)	Count and display all those words which starts with alphabet a/A

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


### Other
Raise an issue on [github](https://github.com/sujaldev/school) to report anything.