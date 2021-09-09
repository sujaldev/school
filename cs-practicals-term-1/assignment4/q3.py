"""
Write a Python program to create a dictionary of students where name is the key, marks is
the value of the dictionary. Create another dictionary from existing one after removing keys
containing duplicate values from the Dictionary.
"""
db = {}
print("Create student database:")
while input("Enter record (y/n): ").lower() == "y":
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    db[name] = marks

unique_values, unique_dict = [], {}
for key, val in db.items():
    if val not in unique_values:
        unique_values.append(val)
        unique_dict[key] = val

print("Unique entries:")
for name, marks in unique_dict.items():
    print(f"{name}: {marks}")
