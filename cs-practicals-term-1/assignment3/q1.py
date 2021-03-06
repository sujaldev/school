"""
WAP to generate and display first n fibonacci numbers in a tuple.
"""
x, n1, n2 = int(input("Enter length of fibonacci series to be displayed: ")), 0, 1

print(f"Fibonacci series till {x}:", n1, n2, sep="\n")
for i in range(x):
    n1, n2 = n2, n1 + n2
    print(n2)

"""
OUTPUT:
Enter length of fibonacci series to be displayed: 10
Fibonacci series till 10:
0
1
1
2
3
5
8
13
21
34
55
89
"""
