# 8)WAF to display the size of a file after removing EOL characters, leading and trailing spaces and blank lines.


def count_and_display():
    file = open("poem.txt")
    output = []
    for line in file.readlines():
        output.append(line.strip().replace('\n', ''))
    print(len("".join(output)), "Bytes")
    file.close()


count_and_display()
