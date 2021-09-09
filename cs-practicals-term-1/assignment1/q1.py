"""
WAP to input a string check whether it is a palindrome string or not.
"""
string = input("Enter a string to check palindrome: ")

is_palindrome = string == string[::-1]
print("Above string is a palindrome." if is_palindrome else "Above string is not a palindrome.")

"""
OUTPUT
Enter a string to check palindrome: mom
Above string is a palindrome.

Enter a string to check palindrome: not
Above string is not a palindrome.
"""