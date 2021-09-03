import pickle


def delete():
    file = open("student.dat", "rb")
    roll_no = int(input("Enter roll no to delete"))
    buffer = []
    try:
        while True:
            student = pickle.load(file)
            current_roll_no = student[0]
            if current_roll_no != roll_no:
                buffer.append(student)
            else:
                print("MATCH FOUND... DELETING...")
    except EOFError:
        file.close()
    file = open("student.dat", "wb")
    for each in buffer:
        pickle.dump(each, file)
