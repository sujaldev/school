# ASSIGNMENT-1 (String)

1. WAP to input a string check whether it is a palindrome string or not.
2. WAP to input a string and print number of upper and lower case vowels in it.
3. WAP to input a string, capitalize every alternate character in a string E.g: original string : computer science new
   string after alternate character in upper : cOmPuTeR ScIeNcE
4. WAP to find the frequency of any particular alphabet in a given string.
5. WAP to input a string and print in the following format :
   E.g. if the given string is ‘hello’ then the output should be as follows :\
   hello\
   hell\
   hel\
   he\
   h

---

# ASSIGNMENT-2 (List)

1. WAP to read a list of numbers. Rearrange the list in such a way that the values of alternate locations of the list
   are exchanged. Example: If the list initially contains 2, 5, 9, 14, 17, 8, 19, 16 Then after rearrangement the list
   should contain 5, 2, 14, 9, 8, 17, 16, 19
2. WAP to read a list of numbers. Replace every element of the list with its reverse. For example: If the list is having
   5 elements. 25 124 7 19 92 Then the program should rearrange the list contents as :
   52 421 7 91 29
3. WAP to read two list of numbers, create third list which contains all elements from given two list alternatively.
4. WAP to arrange a given list of numbers in ascending order using bubble sort.
5. WAP to remove all the odd numbers from a given list.
6. WAP to input a list of numbers arrange the given list in ascending order using insertion sort.

---

# ASSIGNMENT-3(Tuple)

1. WAP to generate and display first n fibonacci numbers in a tuple.

---

# ASSIGNMENT-4(Dictionaries)

1. WAP to store name and total marks in a dictionary by taking input from user and then find Topper or Toppers by
   copying their records in other dictionary.
2. Write a menu driven Program to Store Name and Phone number in a dictionary, Input Name and search his/her phone
   number, Input Phone and search its owner name. Traverse the whole dictionary depending on choice of the user.
3. Write a Python program to create a dictionary of students where name is the key, marks is the value of the
   dictionary. Create another dictionary from existing one after removing keys containing duplicate values from the
   Dictionary. For eg :- If the dictionary is : {'Amit': 12, 'Sim': 10, 'Bhawna': 12, 'Hari': 13} New dictionary =
   {'Amit': 12, 'Sim': 10, 'Hari': 13}
4. WAP to create a dictionary of n employees where names are keys and values of each employee is a collection of BASIC(
   input by the user), DA(20% of Basic), HRA(10% of Basic), TA(10% of Basic). Calculate and display the total salary of
   each employee.

---

# ASSIGNMENT-5(User Defined Functions)

1. WAP to calculate and display binomial coefficient for the given values of n and r using function. [nCr = n!/r!(n-r)!]
2. Write a function to return addition, subtraction, multiplication and division of two numbers received as parameter
   from the calling function display the result.
3. Write a function that receives a number as parameter and return one if it is a palindrome number otherwise return
   zero display the appropriate message.
4. Write a program to calculate and display power of base and exponent that is a raise to power b using user defined
   function. If the exponent is not passed by the user then the square of the given number should be calculated.
   Implement the above program for both situations.
5. Write a function isort() to sort a list of numbers in ascending order using insertion sort where the list is passed
   as parameter. WAP to input a list of numbers sort the list using function and display the result.

---

# ASSIGNMENT-6(Text File)

1. A menu driven program to do the following:
   (a)Display the file 'story.txt'.
   (b)Count and display all the words which starts with alphabet 'a' or 'A' from an existing file
   'story.txt' using read function.
2. Write a menu driven program to do the following:
   (a)Display the file 'story.txt'.
   (b)Count and display all the lines which ends with alphabet 'a' or'A' use readlines function to read the content.
3. Write a menu driven program to do the following:
   (a)Add more lines(one at a time) in an existing file 'story.txt'.
   (b)Display the content of the file using readline function.

---

# ASSIGNMENT-7(Binary File)

1. Write a menu driven program to do the following functions:-
   (a)To create a binary file 'student.dat' containing fields as rno, name, marks and grade in a list.
   (b)Display the details of all those studends who have got grade A.
2. Write a menu driven program to do the following:-
   (a)To create a binary file 'product.dat' in the following format : {‘name’ : ‘file’, ‘price’ : 112}, {‘name’ : ‘pen’,
   ‘price’ : 30}, etc.
   (b)To display the above file
   (c)Transfer all the records from binary file ‘product.dat’ to ‘new.dat’ whose price is less than
3. Write a menu driven program to do the following:-
   (a)To create a binary file 'student.dat' containing fields as rno, name, marks and grade in a list.
   (b)Function to update a record for a given roll number without using another file.
   (c)Display the file after and before updation
4. Write a menu driven program to do the following:-
   (a)To create a binary file 'student.dat' containing fields as rno, name, marks and grade in a list.
   (b)Function to delete a record for a given roll number.
   (c)Display the file after and before updation
5. Write a menu driven program to do the following:-
   (a)To create a binary file 'item.dat' containing fields as item_id, item_name, price, quantity in the following
   format : [[121,pen,20,5],[21,pencil,10,10],.....]
   (b)To display the above file
   (c)Add more item details in the existing file.
   (d)Display the details of an item for a given item_id.

---

# ASSIGNMENT-8(CSV File)

1. Write a menu driven program to do the following :
   (a)Create a csv file 'book.csv' containing book record as book_no, book_name, author_name and cost.
   (b)Display the file.
   (c)Update the details of a book for the given book number.
2. Write a menu driven program to do the following :
   (a)Create a csv file 'item.csv' containing item record as item_no, item_name, cost and quantity.
   (b)Display the file.
   (c)Delete an item where the item number is given by the user.
3. WAF to search and display the record of that product from the file ‘product.csv’ which has maximum cost. Sample of
   ‘product.csv’ is shown below :
   PID, PNAME, COST, QUANTITY P1, BRUSH, 50, 200 P2, TOOTHPASTE, 120, 150 P3, COMB, 40, 300 P4, SHEETS, 100, 500
4. WAF to transfer only those records from the file product.csv to another file ‘pro1.csv’ whose quantity is more than
   150. Also include the first row with headings sample of product.csv is shown below :
   PID, PNAME, COST, QUANTITY P1, BRUSH, 50, 200 P2, TOOTHPASTE, 120, 150 P3, COMB, 40, 300 P4, SHEETS, 100, 500