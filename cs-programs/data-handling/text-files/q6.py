# 6)WAF to count and display number of words in each line of text file "first.txt".

def count_words():
    file = open("first.txt")
    i = 1
    for line in file.readlines():
        print(f"{len(line)} words at line no {i}")
        i += 1
    file.close()


count_words()
