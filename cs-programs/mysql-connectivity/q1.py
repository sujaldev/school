"""
Q1) WAP to retrieve and display all the employees working in a given department
entered by the user at run from an existing table employee in a database sample
"""

import mysql.connector as sql


connection = sql.connect(host="127.0.0.1", user="root", database="emp", password="Sujal@5243")
c = connection.cursor()

c.execute(f"SELECT * FROM employee WHERE deptno={input('Enter Department Number: ')}")
data = [e[1] for e in c.fetchall()]
print("\n".join(data if data else ["No record found"]))

"""
# OUTPUT

Enter Department Number: 20
Smith
Jones
Scott
Adams
Ford

Enter Department Number: 1
No record found

"""
