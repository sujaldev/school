"""
Write a menu driven program to do the following:
    a) Add more lines(one at a time) in an existing file 'story.txt'.
    b) Display the content of the file using readline function.
"""


def append_lines():
    story = open("story.txt", "a")
    while input("Enter lines (y/n): ").lower() == "y":
        story.write("\n" + input("Enter line: "))
    story.close()


def display():
    try:
        story = open("story.txt")
        line = story.readline()
        while line:
            print(line, end="")
            line = story.readline()
        print("\n")
        story.close()
    except FileNotFoundError:
        print("No such file exits...")


def menu():
    while True:
        print("1. Append lines to 'story.txt'",
              "2. Display 'story.txt' line by line",
              "3. Exit", sep="\n")
        choice = input("Enter choice: ")

        if choice == "1":
            append_lines()
        elif choice == "2":
            display()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again...")


menu()

"""
OUTPUT:
1. Append lines to 'story.txt'
2. Display 'story.txt' line by line
3. Exit
Enter choice: 1
Enter lines (y/n): y
Enter line: this is appended line 1
Enter lines (y/n): y
Enter line: this is appended line 2
Enter lines (y/n): n
1. Append lines to 'story.txt'
2. Display 'story.txt' line by line
3. Exit
Enter choice: 2
Hello astronaut
Ola Amigos!
this is a line that ends with an A
on the other hand this ends with an a
this is appended line 1
this is appended line 2

1. Append lines to 'story.txt'
2. Display 'story.txt' line by line
3. Exit
Enter choice: 3
Exiting...
"""
