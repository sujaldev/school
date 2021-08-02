import pickle


def delete():
    file = open("student.dat", "rb+")
    rn = int(input("Enter roll no to delete"))
    buffer = []
    try:
        while True:
            r = pickle.load(file)
            if r[0] != rn:
                buffer.append(r)
            else:
                print("MATCH FOUND... DELETING...")
    except EOFError:
        pass
    file.truncate(0)
    for each in buffer:
        pickle.dump(each, file)
