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