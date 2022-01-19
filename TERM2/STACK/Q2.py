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

"""
OUTPUT:
String To Reverse: hello world
PUSHED -> h
PUSHED -> e
PUSHED -> l
PUSHED -> l
PUSHED -> o
PUSHED ->  
PUSHED -> w
PUSHED -> o
PUSHED -> r
PUSHED -> l
PUSHED -> d
POPPED <- d
POPPED <- l
POPPED <- r
POPPED <- o
POPPED <- w
POPPED <-  
POPPED <- o
POPPED <- l
POPPED <- l
POPPED <- e
POPPED <- h
OUTPUT:  dlrow olleh
"""
