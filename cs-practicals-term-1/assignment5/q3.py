"""
Write a function that receives a number as parameter and return one if it is a palindrome
number otherwise return zero display the appropriate message.
"""


def is_palindrome(number):
    number = str(number)
    return 1 if number == number[::-1] else 0


num = int(input("Enter a number to check if it is a palindrome: "))
print("Number is a palindrome" if is_palindrome(num) else "Number is not a palindrome")
