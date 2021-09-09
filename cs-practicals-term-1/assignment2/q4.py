"""
WAP to arrange a given list of numbers in ascending order using bubble sort.
"""
l = eval(input('Enter a list: '))
length = len(l) - 1
for i in range(length):
    for j in range(length - i):
        if l[j] > l[j + 1]:
            l[j], l[j + 1] = l[j + 1], l[j]

print('Sorted list: ', l)

"""
OUTPUT:
Enter a list: [5, 4, 3, 2, 1]
Sorted list:  [1, 2, 3, 4, 5]
"""
