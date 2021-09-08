string = input("Enter string: ")
length = len(string)

for i in range(length):
    space = " " * i
    letters = string[:length - i]
    print(space + letters)
