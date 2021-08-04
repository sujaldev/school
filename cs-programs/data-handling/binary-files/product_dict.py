"""
Q15) WAP to menu driven program to do the following:-
    (a) Create a binary file 'product.dat' in the following format
    {‘name’ : ‘file’, ‘price’ : 112}, {‘name’ : ‘pen’, ‘price’ : 30},etc.
    (b) Display the above file
    (c) Transfer all the records from binary file ‘product.dat’ to ‘new.dat’ whose price is less than 100.
"""
import pickle


def create():
    file = open("product.dat", "wb")
    while input("Enter values (y/n): ").lower() == "y":
        pickle.dump({
            "name": input("Enter name: "),
            "price": float(input("Enter price: "))
        }, file)
    file.close()


def display():
    try:
        file = open("product.dat", "rb")
        try:
            while True:
                data = pickle.load(file)
                print("\n"
                      f"NAME: {data['name']}",
                      f"PRICE: {data['price']}",
                      sep="\n"
                      )
        except EOFError:
            print("ALL RECORDS PRINTED")
        file.close()
    except FileNotFoundError:
        print("FILE DOES NOT EXIST YET, CREATE IT FIRST.")


def transfer():
    try:
        p_file, o_file = open("product.dat", "rb"), open("new.dat", "wb")
        try:
            while True:
                data = pickle.load(p_file)
                if data["price"] < 100:
                    pickle.dump(data, o_file)
        except EOFError:
            print("TRANSFER COMPLETE...")
    except FileNotFoundError:
        print("PRODUCT FILE DOESN'T EXIST YET, CREATE IT FIRST.")


def menu():
    while True:
        print("\n",
              "1: CREATE FILE",
              "2: DISPLAY FILE",
              "3: TRANSFER CHEAP PRODUCTS",
              "4: EXIT",
              "\n", sep="\n")

        choice = input("Enter choice: ")

        if choice == "1":
            create()
        elif choice == "2":
            display()
        elif choice == "3":
            transfer()
        elif choice == "4":
            break
        else:
            print("INVALID CHOICE... TRY AGAIN...")


menu()
