# 5)WAF to display the number of characters of file ‘first.txt’ without counting EOL characters.

def count_char():
    file = open("first.txt")
    char_count = len(file.read().replace("\n", ""))
    print(f"There are {char_count} characters in the file first.txt")
    file.close()


count_char()
