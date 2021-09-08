# SCHOOL RESOURCES ARCHIVE

All school related resources stored here.

#### THIS WEBSITE IS MAINTAINED BY SUJAL SINGH

### RESOURCE LIST

## <br>WAP to calculate and display binomial coefficient for the given values of n and r using<br>function. [nCr = n!/r!(n-r)!]<br>
```python
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

```
## <br>Write a function to return addition, subtraction, multiplication and division of two numbers<br>received as parameter from the calling function display the result.<br>
```python
"""
Write a function to return addition, subtraction, multiplication and division of two numbers
received as parameter from the calling function display the result.
"""


def do_ops(a, b):
    return (a + b, "+"), (a - b, "-"), (a * b, "*"), (a / b, "/")


num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
for result, operator in do_ops(num1, num2):
    print(f"{num1} {operator} {num2} = {result}")

```


---

### [RAISE AN ISSUE](https://github.com/sujaldev/school/issues/new/choose) ON GITHUB IF

- Answer is wrong
- Want a missing question to be added
- Need help with a question
- Need help navigating the website
- Website has a bug

### WANT TO CONTRIBUTE RESOURCES?

Fork my [repository](https://github.com/sujaldev/school) \
After adding changes, create a pull request.