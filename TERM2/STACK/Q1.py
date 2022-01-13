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
