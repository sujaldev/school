"""
WAP to remove all the odd numbers from a given list.
"""
l = eval(input("Enter a list: "))
even_list = [e for e in l if e % 2 == 0]
print("Sorted list: ", even_list)

"""
OUTPUT:

Enter a list: [1, 2, 3, 4, 5, 6, 7, 8, 9]
Sorted list:  [2, 4, 6, 8]
"""
