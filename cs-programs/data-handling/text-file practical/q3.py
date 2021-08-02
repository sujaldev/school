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
