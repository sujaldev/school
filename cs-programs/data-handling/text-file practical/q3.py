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
