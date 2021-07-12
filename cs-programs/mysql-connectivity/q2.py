"""
Q2) WAP to create a table game (game no, name , nop) and insert rows in it
using  user defined functions create_table() and insert_rows()
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
    "game_no int primary key",
    "game_name varchar(20)",
    "nop int"
))

while True:
    insert_values("game", (
        input("Enter game no: "),
        f'"{input("Enter game name: ")}"',
        input("Enter no. of players: ")
    ))
    if input("Continue (y/n): ").lower() != "y":
        break

connection.close()

"""
# OUTPUT

Enter game no: 1
Enter game name: football
Enter no. of players: 22
Continue (y/n): y
Enter game no: 2
Enter game name: basketball
Enter no. of players: 18
Continue (y/n): y
Enter game no: 3
Enter game name: volleyball
Enter no. of players: 12
Continue (y/n): n


"""