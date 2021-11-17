"""
Q3) Write program in Python to do the following (using user defined functions):
    a) Create a CSV file containing word and its meaning.
    b) Determine the meaning for the given word.
    c) To display all word and meanings
"""
import csv


def create():
    rows = []
    while input("Enter values (y/n): ").lower() == "y":
        rows.append([
            input("Enter word: ").lower(),
            input("Enter meaning of word: ")
        ])

    with open("dictionary.csv", "w", newline="") as file:
        csv.writer(file).writerows(rows)


def find_meaning():
    word = input("Enter the word you are looking for: ").lower()
    with open("dictionary.csv", newline="") as file:
        data = [w for w in csv.reader(file) if w[0] == word]

    if data:
        print("{} means: {}".format(*data[0]))
    else:
        print("No such word found.")


def display():
    with open("dictionary.csv", newline="") as file:
        data = csv.reader(file)
        for word in data:
            print("{}: {}".format(*word))


def menu():
    while True:
        choice = input(
            "\n\n"
            "1. Create Dictionary\n"
            "2. Find meaning of a word\n"
            "3. Display all words\n"
            "4. Exit\n"
            "Enter your choice: "
        )

        if choice == "1":
            create()
        elif choice == "2":
            find_meaning()
        elif choice == "3":
            display()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice... Try again...")


menu()
