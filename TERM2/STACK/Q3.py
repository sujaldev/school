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
