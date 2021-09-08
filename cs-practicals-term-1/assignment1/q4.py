"""
WAP to find the frequency of any particular alphabet in a given string
"""

frequency = input("Enter a string:  ").count(
    input("Enter a character to check it's frequency in above string: ")
)

print(f"The above character occurs {frequency} times in given string.")
