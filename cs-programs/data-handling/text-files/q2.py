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
