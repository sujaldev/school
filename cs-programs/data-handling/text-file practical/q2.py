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
