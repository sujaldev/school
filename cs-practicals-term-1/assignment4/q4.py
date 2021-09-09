"""
WAP to create a dictionary of n employees where names are keys and values of each
employee is a collection of BASIC(input by the user), DA(20% of Basic), HRA(10% of Basic),
TA(10% of Basic). Calculate and display the total salary of each employee.
"""
while input("Enter more employees (y/n): ").lower() == "y":
    basic = int(input("Enter basic: "))
    da = 0.2 * basic
    hra = ta = 0.1 * basic
    print("Total salary:", basic + da + hra + ta)

"""
OUTPUT:
Enter more employees (y/n): y
Enter basic: 200
Total salary: 280.0
Enter more employees (y/n): y
Enter basic: 300
Total salary: 420.0
Enter more employees (y/n): n
"""
