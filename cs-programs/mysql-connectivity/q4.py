"""
Q4) WAP TO:
A) CREATE THE GIVEN TABLE ORDERS
B) ADD VALUES TO THE TABLE WITH VALUES FROM USER TAKEN AT RUNTIME
C) DELETE A RECORD FROM TABLE FOR A GIVEN ORDER NUMBER
D) DISPLAY ALL RECORDS
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


def delete_order_by_no(order_no, table_name="orders"):
    try:
        c.execute(f"DELETE FROM {table_name} WHERE order_no={order_no}")
    except Exception as e:
        print("An error occurred:\n", e)


def display_record(table_name):
    try:
        c.execute(f"SELECT * FROM {table_name};")
        data = [c.column_names] + c.fetchall()
        space, buffer = [], []

        # GET PADDING
        for column in range(len(data[0])):
            for row in range(len(data)):
                buffer.append(len(str(data[row][column])))
            space, buffer = space + [max(buffer)], []

        table_width = sum([extra + 4 for extra in space])

        # PRINT OUT TABLE
        print("━" * table_width)

        for row in range(len(data)):
            print("┃ ", end="")
            for column in range(len(data[row])):
                entry = str(data[row][column])
                entry = entry + " " * (space[column] - len(entry))
                print(f"{entry} ┃  ", end="")
            print("\n", "━" * table_width, sep="")

        # print("‾" * table_width)
    except Exception as e:
        print("An error occurred:\n", e)


create_table("orders", (
    "order_no int(10)",
    "client_name varchar(30)",
    "client_loc varchar(30)",
    "orders int(10)",
    "payments int(10)"
))

while True:
    insert_values("orders", (
        input("Enter Order no: "),
        f'"{input("Enter client name: ")}"',
        f'"{input("Enter client loc: ")}"',
        input("Enter orders: "),
        input("Enter payments: ")
    ))
    if input("Continue adding? (y/n): ").lower() != "y":
        break

while True:
    delete_order_by_no(int(input("Enter order no to delete: ")))
    if input("Continue deleting? (y/n): ").lower() != "y":
        break
display_record("orders")
connection.close()


"""
# OUTPUT QUESTION 4

Enter Order no: 1
Enter client name: sujal
Enter client loc: test
Enter orders: 2
Enter payments: 3
Continue adding? (y/n): y

Enter Order no: 2
Enter client name: feynman
Enter client loc: test
Enter orders: 3
Enter payments: 4
Continue adding? (y/n): y

Enter Order no: 3
Enter client name: hilbert
Enter client loc: test
Enter orders: 4
Enter payments: 5
Continue adding? (y/n): y

Enter Order no: 4
Enter client name: neumann
Enter client loc: test
Enter orders: 5
Enter payments: 6
Continue adding? (y/n): n

Enter order no to delete: 3
Continue deleting? (y/n): n

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┃ order_no ┃  client_name ┃  client_loc ┃  orders ┃  payments ┃  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┃ 1        ┃  sujal       ┃  test       ┃  2      ┃  3        ┃  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┃ 2        ┃  feynman     ┃  test       ┃  3      ┃  4        ┃  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
┃ 4        ┃  neumann     ┃  test       ┃  5      ┃  6        ┃  
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

"""