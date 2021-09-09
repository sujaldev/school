"""
WAP to read two list of numbers, create third list which contains all elements from given
two list alternatively.
"""

l1 = eval(input("Enter first list: "))
l2 = eval(input("Enter second list: "))
merged = []

for i in range(len(max(l1, l2))):
    if i < len(l1):
        merged.append(l1[i])
    if i < len(l2):
        merged.append(l2[i])

print(merged)

"""
OUTPUT:
Enter first list: [1, 3, 5]
Enter second list: [2, 4, 6]
[1, 2, 3, 4, 5, 6]

Enter first list: [1, 2, 3]
Enter second list: [2, 4, 6, 7, 8, 9]
[1, 2, 2, 4, 3, 6, 7, 8, 9]
"""