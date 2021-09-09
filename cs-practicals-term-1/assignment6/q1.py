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
