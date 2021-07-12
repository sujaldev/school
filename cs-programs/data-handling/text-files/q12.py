# 12)WAF to count and display the words ending with ‘e’ in a text file ‘poem.txt’.

def count_e():
    file = open("poem.txt")
    count = 0
    for word in file.read().replace("\n", " ").split(" "):
        if word.endswith("e"):
            count += 1
    print(f"{count} words in poem.txt end with e")
    file.close()


count_e()
