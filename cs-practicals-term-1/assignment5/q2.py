"""
Write a function to return addition, subtraction, multiplication and division of two numbers
received as parameter from the calling function display the result.
"""


def do_ops(a, b):
    return (a + b, "+"), (a - b, "-"), (a * b, "*"), (a / b, "/")


num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
for result, operator in do_ops(num1, num2):
    print(f"{num1} {operator} {num2} = {result}")

"""
OUTPUT:
Enter first number: 2
Enter second number: 3
2.0 + 3.0 = 5.0
2.0 - 3.0 = -1.0
2.0 * 3.0 = 6.0
2.0 / 3.0 = 0.6666666666666666
"""
