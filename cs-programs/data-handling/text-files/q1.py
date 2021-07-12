# 1)WAP to create a text file of story.txt with one line at a time. Display the file.

def create_file():
    file = open("story.txt", "w")
    while input("Enter values (y/n): ").lower() == "y":
        file.write(input("Enter text: ") + "\n")
    file.close()


create_file()
