"""
WAP to input a string and print in the following format
E.g. if the given string is ‘hello’ then the output should be as follows:
hello
 hell
  hel
   he
    h
"""
string = input("Enter string: ")
length = len(string)

for i in range(length):
    space = " " * i
    letters = string[:length - i]
    print(space + letters)

"""
OUTPUT:
Enter string: hello
hello
 hell
  hel
   he
    h
"""
