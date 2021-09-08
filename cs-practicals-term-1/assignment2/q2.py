"""
WAP to read a list of numbers. Replace every element of the list with its reverse.
    For example: If the list is having 5 elements.
        25 124 7 19 92
    Then the program should rearrange the list contents as :
        52 421 7 91 29
"""
l = eval(input("Enter a List: "))
print(", ".join([str(e)[::-1] for e in l]))
