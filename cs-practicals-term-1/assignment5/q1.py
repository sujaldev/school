"""
WAP to calculate and display binomial coefficient for the given values of n and r using
function. [nCr = n!/r!(n-r)!]
"""


def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


def binomial(n, r):
    if n == r:
        return 1
    else:
        return fact(n) // (fact(r) * fact(n - r))


n_val = float(input("Enter value for n: "))
r_val = float(input("Enter value for r: "))
print("Binomial is: ", binomial(n_val, r_val))

"""
OUTPUT:
Enter value for n: 2
Enter value for r: 2
Binomial is:  1
"""
