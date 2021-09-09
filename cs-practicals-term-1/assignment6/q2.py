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
