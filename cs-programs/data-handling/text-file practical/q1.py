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
