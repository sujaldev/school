"""
WAP to input a list of numbers arrange the given list in ascending order using insertion sort.
"""
l = eval(input("Enter a list:"))
length = len(l)
for i in range(1, length):
    temp = l[i]
    j = i - 1
    while l[j] > temp and j >= 0:
        l[j + 1] = l[j]
        j -= 1
    l[j + 1] = temp

print("Sorted list: ", l)

"""
OUTPUT:
Enter a list: [5, 4, 3, 2, 1]
Sorted list:  [1, 2, 3, 4, 5]
"""
