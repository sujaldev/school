"""
Write a program to calculate and display power of base and exponent that is a raise to
power b using user defined function. If the exponent is not passed by the user then the
square of the given number should be calculated. Implement the above program for both
situations.
"""


def power():
    b, e = int(input("Enter base: ")), int(input("Enter power (or leave emtpy to use default): ") or 2)
    result = b

    for i in range(1, e):
        result *= b
    print(result)


power()
