"""
WAP to read a list of numbers. Rearrange the list in such a way that the values of alternate
locations of the list are exchanged.
    Example: If the list initially contains
        2, 5, 9, 14, 17, 8, 19, 16
    Then after rearrangement the list should contain
        5, 2, 14, 9, 8, 17, 16, 19
"""

l = eval(input("Enter a list: "))
length = len(l) if (len(l) % 2 == 0) else len(l) - 2

for i in range(0, length, 2):
    l[i], l[i + 1] = l[i + 1], l[i]
print(l)
