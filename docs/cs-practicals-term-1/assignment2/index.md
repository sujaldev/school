# SCHOOL RESOURCES ARCHIVE

All school related resources stored here.

#### THIS WEBSITE IS MAINTAINED BY SUJAL SINGH

### RESOURCE LIST

## <br>WAP to read a list of numbers. Rearrange the list in such a way that the values of alternate<br>locations of the list are exchanged.<br>    Example: If the list initially contains<br>        2, 5, 9, 14, 17, 8, 19, 16<br>    Then after rearrangement the list should contain<br>        5, 2, 14, 9, 8, 17, 16, 19<br>
```python
"""
WAP to read a list of numbers. Rearrange the list in such a way that the values of alternate
locations of the list are exchanged.
    Example: If the list initially contains
        2, 5, 9, 14, 17, 8, 19, 16
    Then after rearrangement the list should contain
        5, 2, 14, 9, 8, 17, 16, 19
"""

l = eval(input("Enter a list: "))
length = len(l) if (len(l) % 2 == 0) else len(l) - 2

for i in range(0, length, 2):
    l[i], l[i + 1] = l[i + 1], l[i]
print(l)

"""
OUTPUT:
Enter a list: [1, 2, 3, 4, 5, 6]
[2, 1, 4, 3, 6, 5]

Enter a list: [1, 2, 3, 4, 5]
[2, 1, 4, 3, 5]
"""
```
## <br>WAP to read a list of numbers. Replace every element of the list with its reverse.<br>    For example: If the list is having 5 elements.<br>        25 124 7 19 92<br>    Then the program should rearrange the list contents as :<br>        52 421 7 91 29<br>
```python
"""
WAP to read a list of numbers. Replace every element of the list with its reverse.
    For example: If the list is having 5 elements.
        25 124 7 19 92
    Then the program should rearrange the list contents as :
        52 421 7 91 29
"""
l = eval(input("Enter a List: "))
print(", ".join([str(e)[::-1] for e in l]))

"""
OUTPUT:

"""
```
## <br>WAP to read two list of numbers, create third list which contains all elements from given<br>two list alternatively.<br>
```python
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
```
## <br>WAP to arrange a given list of numbers in ascending order using bubble sort.<br>
```python
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

```
## <br>WAP to remove all the odd numbers from a given list.<br>
```python
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

```
## <br>WAP to input a list of numbers arrange the given list in ascending order using insertion sort.<br>
```python
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

```


---

### [RAISE AN ISSUE](https://github.com/sujaldev/school/issues/new/choose) ON GITHUB IF

- Answer is wrong
- Want a missing question to be added
- Need help with a question
- Need help navigating the website
- Website has a bug

### WANT TO CONTRIBUTE RESOURCES?

Fork my [repository](https://github.com/sujaldev/school) \
After adding changes, create a pull request.

<script src="https://giscus.app/client.js"
        data-repo="sujaldev/school"
        data-repo-id="MDEwOlJlcG9zaXRvcnkzODUzMDMzOTI="
        data-category="Q&A"
        data-category-id="DIC_kwDOFvdDYM4CArKZ"
        data-mapping="pathname"
        data-reactions-enabled="1"
        data-emit-metadata="0"
        data-theme="light"
        data-lang="en"
        crossorigin="anonymous"
        async>
</script>