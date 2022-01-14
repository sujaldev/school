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

"""
OUTPUT:
Enter value for n: 2
Enter value for r: 2
Binomial is:  1
"""

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

"""
OUTPUT:
Enter first number: 2
Enter second number: 3
2.0 + 3.0 = 5.0
2.0 - 3.0 = -1.0
2.0 * 3.0 = 6.0
2.0 / 3.0 = 0.6666666666666666
"""

```
## <br>Write a function that receives a number as parameter and return one if it is a palindrome<br>number otherwise return zero display the appropriate message.<br>
```python
"""
Write a function that receives a number as parameter and return one if it is a palindrome
number otherwise return zero display the appropriate message.
"""


def is_palindrome(number):
    number = str(number)
    return 1 if number == number[::-1] else 0


num = int(input("Enter a number to check if it is a palindrome: "))
print("Number is a palindrome" if is_palindrome(num) else "Number is not a palindrome")

"""
OUTPUT:
Enter a number to check if it is a palindrome: 121
Number is a palindrome

Enter a number to check if it is a palindrome: 1223
Number is not a palindrome
"""

```
## <br>Write a program to calculate and display power of base and exponent that is a raise to<br>power b using user defined function. If the exponent is not passed by the user then the<br>square of the given number should be calculated. Implement the above program for both<br>situations.<br>
```python
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

"""
OUTPUT:
Enter base: 2
Enter power (or leave emtpy to use default): 2
4

Enter base: 4
Enter power (or leave emtpy to use default): 
16
"""

```
## <br>Write a function isort() to sort a list of numbers in ascending order using insertion sort<br>where the list is passed as parameter. WAP to input a list of numbers sort the list using<br>function and display the result.<br>
```python
"""
Write a function isort() to sort a list of numbers in ascending order using insertion sort
where the list is passed as parameter. WAP to input a list of numbers sort the list using
function and display the result.
"""


def isort(l):
    length = len(l)
    for i in range(1, length):
        temp = l[i]
        j = i - 1
        while l[j] > temp and j >= 0:
            l[j + 1] = l[j]
            j -= 1
        l[j + 1] = temp
    return l


unsorted = eval(input("Enter a list: "))
print("Sorted list: ", isort(unsorted))

"""
OUTPUT:
Enter a list: [5, 4, 3, 2, 1]
Sorted list:  [1, 2, 3, 4, 5]
"""
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

<script src="https://giscus.app/client.js"
        data-repo="sujaldev/school"
        data-repo-id="MDEwOlJlcG9zaXRvcnkzODUzMDMzOTI="
        data-category="Q&A"
        data-category-id="DIC_kwDOFvdDYM4CArKZ"
        data-mapping="pathname"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-theme="light"
        data-lang="en"
        crossorigin="anonymous"
        async>
</script>