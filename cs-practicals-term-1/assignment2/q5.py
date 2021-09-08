"""
WAP to remove all the odd numbers from a given list.
"""
l = eval(input("Enter a list: "))
even_list = [e for e in l if e % 2 == 0]
print(even_list)
