# SCHOOL RESOURCES ARCHIVE

All school related resources stored here.

#### THIS WEBSITE IS MAINTAINED BY SUJAL SINGH

### RESOURCE LIST

## <br>1. Write a menu-driven python program to implement a stack of marks using user defined function :<br>   (a) PUSH() to push marks of a student in a stack.<br>   (b) POP() an element from the stack.<br>   (c) Display the stack of marks.<br>
```python
"""
1. Write a menu-driven python program to implement a stack of marks using user defined function :
   (a) PUSH() to push marks of a student in a stack.
   (b) POP() an element from the stack.
   (c) Display the stack of marks.
"""
stack = []
top = -1


def push():
    global top
    elem = int(input("Enter Marks: "))
    stack.append(elem)
    top += 1
    print("PUSHED ->", elem)


def pop():
    global top
    if not stack:
        print("Stack underflow (stack is empty)")
    else:
        elem = stack.pop()
        top -= 1
        print("POPPED <-", elem)


def display():
    global top
    if not stack:
        print("Stack underflow (stack is emtpy)")
    else:
        print("-------STACK START----------")
        print(stack[top], '<- top')
        for i in range(top - 1, -1, -1):
            print(stack[i])
        print("-------STACK  END----------")


while True:
    choice = input(
        "1. Push\n"
        "2. Pop\n"
        "3. Display\n"
        "4. Exit\n"
        "\nYour Choice: "
    )
    if choice == "1":
        push()
        print('TOP: ', top)
    elif choice == "2":
        pop()
        print('TOP: ', top)
    elif choice == "3":
        display()
    elif choice == "4":
        break
    else:
        print("Invalid Choice...")

```
## <br>2. WAP to reverse a string using PUSH and POP operation in Stack.<br>
```python
"""
2. WAP to reverse a string using PUSH and POP operation in Stack.
"""
stack = []
top = -1


def push(elem):
    global top
    stack.append(elem)
    top += 1
    print("PUSHED ->", elem)


def pop():
    global top
    if not stack:
        print("Stack underflow (stack is empty)")
    else:
        elem = stack.pop()
        top -= 1
        print("POPPED <-", elem)
        return elem


def reverse_string():
    string = input("String To Reverse: ")
    [push(char) for char in string]

    reverse = ""
    for i in range(len(string)):
        reverse += pop()

    print("OUTPUT: ", reverse)


reverse_string()

```
## <br>3. Write a program to create a Stack for storing only odd numbers out of all the numbers entered by the user.<br>Display the content of the Stack along with the largest odd number in the Stack.<br>(Hint : Keep popping out the elements from stack and maintain the largest element retrieved so far in a variable.<br>Repeat till Stack is empty)<br>
```python
"""
3. Write a program to create a Stack for storing only odd numbers out of all the numbers entered by the user.
Display the content of the Stack along with the largest odd number in the Stack.
(Hint : Keep popping out the elements from stack and maintain the largest element retrieved so far in a variable.
Repeat till Stack is empty)
"""
stack = []
top = -1


def push(elem):
    global top
    stack.append(elem)
    top += 1
    print("PUSHED ->", elem)


def pop():
    global top
    if not stack:
        print("Stack underflow (stack is empty)")
    else:
        elem = stack.pop()
        top -= 1
        print("POPPED <-", elem)
        return elem


def display():
    global top
    if not stack:
        print("Stack underflow (stack is emtpy)")
    else:
        print("-------STACK START----------")
        print(stack[top], '<- top')
        for i in range(top - 1, -1, -1):
            print(stack[i])
        print("-------STACK  END----------")


def odd_input():
    largest_elem = None
    while input("Enter numbers (y/n): ").lower() == "y":
        num = int(input("Enter number: "))
        if largest_elem is None:
            largest_elem = num
        if num % 2 != 0:
            push(num)
            largest_elem = max(num, largest_elem)


odd_input()
print("Stack: ")
display()

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