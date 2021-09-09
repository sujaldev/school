"""
WAP to input a string and print number of upper and lower case vowels in it.
"""
string = input("Enter a string: ")

upper_count, lower_count = 0, 0
for letter in string:
    if letter in ("A", "E", "I", "O", "U"):
        upper_count += 1
    elif letter in ("a", "e", "i", "o", "u"):
        lower_count += 1

print(f"The given string has {upper_count} uppercase vowels and {lower_count} lowercase vowels.")

"""
OUTPUT:
Enter a string: hEllo thIs is a string
The given string has 2 uppercase vowels and 4 lowercase vowels.
"""