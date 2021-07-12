"""
WAP TO INTERFACE BETWEEN PYTHON AND MYSQL TO DO THE FOLLOWING

1) TO CREATE A TABLE GAME IN MYSQL
2) ADD RECORDS IN BY TAKING VALUES AT RUNTIME FROM USER
3) TO DISPLAY ALL STUDENTS WHO HAVE GOT A PARTICULAR GRADE WHICH IS INPUT BY THE USER
"""

import mysql.connector as sql


connection = sql.connect(host="127.0.0.1", user="root", password="Sujal@5243", database="assignment", autocommit=True)
c = connection.cursor()


def create_table(table_name, schema):
    try:
        c.execute(f"CREATE TABLE {table_name} ({','.join(schema)});")
    except Exception as e:
        print("An error occurred:\n", e)


def insert_values(table_name, values):
    try:
        c.execute(f"INSERT INTO {table_name} VALUES({','.join(values)});")
    except Exception as e:
        print("An error occurred:\n", e)


create_table("game", (
    "class int",
    "name varchar(20) not null",
    "game varchar(20)",
    "grade varchar(20) not null"
))


while True:
    insert_values("game", (
        input("Enter class number: "),
        f'"{input("Enter student name: ")}"',
        f'"{input("Enter game: ")}"',
        f'"{input("Enter grade: ").upper()}"'
    ))
    if input("Continue adding? (y/n): ").lower() != "y":
        break


while True:
    grade = input("Enter grade to look for: ")
    c.execute(f"SELECT name FROM game WHERE grade='{grade.upper()}';")
    table = [std[0] for std in c.fetchall()]
    print("\n".join(table if table else ["No record found"]))
    if input("Continue searching? (y/n): ").lower() != "y":
        break

connection.close()

"""
# OUTPUT

Enter class number: 10
Enter student name: sujal
Enter game: football
Enter grade: a
Continue adding? (y/n): y
Enter class number: 11
Enter student name: feynman
Enter game: basketball
Enter grade: a
Continue adding? (y/n): y
Enter class number: 12
Enter student name: hilbert
Enter game: volleyball
Enter grade: b
Continue adding? (y/n): n
Enter grade to look for: a
sujal
feynman
Continue searching? (y/n): n
"""
