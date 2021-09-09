"""
WAP to store name and total marks in a dictionary by taking input from user and then find
Topper or Toppers by copying their records in other dictionary.
"""
student_data, topper_data = {}, {}
table_spacing = 20

while input("Enter records (y/n): ").lower() == "y":
    name, marks = input("Enter student name: "), float(input("Enter student marks: "))
    student_data[name] = marks

print("\nToppers:")
print("Name".center(20), "Marks".center(20), sep="|")
print("_" * 42)
for name, marks in student_data.items():
    if marks >= 90:
        print(name.center(20), str(marks).center(20), sep="|")
        topper_data[name] = marks

"""
OUTPUT:
Enter records (y/n): y
Enter student name: feynman
Enter student marks: 99
Enter records (y/n): y
Enter student name: turing
Enter student marks: 85
Enter records (y/n): n

Toppers:
        Name        |       Marks        
__________________________________________
      feynman       |        99.0       
"""
