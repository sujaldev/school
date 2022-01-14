# SCHOOL RESOURCES ARCHIVE

All school related resources stored here.

#### THIS WEBSITE IS MAINTAINED BY SUJAL SINGH

### RESOURCE LIST

## <br>WAP to input a string check whether it is a palindrome string or not.<br>
```python
"""
WAP to input a string check whether it is a palindrome string or not.
"""
string = input("Enter a string to check palindrome: ")

is_palindrome = string == string[::-1]
print("Above string is a palindrome." if is_palindrome else "Above string is not a palindrome.")

"""
OUTPUT
Enter a string to check palindrome: mom
Above string is a palindrome.

Enter a string to check palindrome: not
Above string is not a palindrome.
"""
```
## <br>WAP to input a string and print number of upper and lower case vowels in it.<br>
```python
"""
WAP to input a string and print number of upper and lower case vowels in it.
"""
string = input("Enter a string: ")

upper_count, lower_count = 0, 0
for letter in string:
    if letter in ("A", "E", "I", "O", "U"):
        upper_count += 1
    elif letter in ("a", "e", "i", "o", "u"):
        lower_count += 1

print(f"The given string has {upper_count} uppercase vowels and {lower_count} lowercase vowels.")

"""
OUTPUT:
Enter a string: hEllo thIs is a string
The given string has 2 uppercase vowels and 4 lowercase vowels.
"""
```
## <br>WAP to input a string, capitalize every alternate character in a string<br>E.g: original string : computer science<br> new string after alternate character in upper : cOmPuTeR ScIeNcE<br>
```python
"""
WAP to input a string, capitalize every alternate character in a string
E.g: original string : computer science
 new string after alternate character in upper : cOmPuTeR ScIeNcE
"""
char_list = list(input("Enter a string: "))

for i in range(1, len(char_list), 2):
    char_list[i - 1] = char_list[i - 1].lower()
    char_list[i] = char_list[i].upper()

print("Alternate Case: ")
print("".join(char_list))

"""
OUTPUT:
Enter a string: computer science
Alternate Case: 
cOmPuTeR ScIeNcE
"""

```
## <br>WAP to find the frequency of any particular alphabet in a given string<br>
```python
"""
WAP to find the frequency of any particular alphabet in a given string
"""

frequency = input("Enter a string:  ").count(
    input("Enter a character to check it's frequency in above string: ")
)

print(f"The above character occurs {frequency} times in given string.")

"""
OUTPUT:
Enter a string:  hello this is a string
Enter a character to check it's frequency in above string: i
The above character occurs 3 times in given string.
"""
```
## <br>WAP to input a string and print in the following format<br>E.g. if the given string is ‘hello’ then the output should be as follows:<br>hello<br> hell<br>  hel<br>   he<br>    h<br>
```python
"""
WAP to input a string and print in the following format
E.g. if the given string is ‘hello’ then the output should be as follows:
hello
 hell
  hel
   he
    h
"""
string = input("Enter string: ")
length = len(string)

for i in range(length):
    space = " " * i
    letters = string[:length - i]
    print(space + letters)

"""
OUTPUT:
Enter string: hello
hello
 hell
  hel
   he
    h
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