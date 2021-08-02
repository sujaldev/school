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
