# 9)WAF to reverse and display each line of text from a already created text file ‘poem.txt’.

def reverse():
    file = open("poem.txt")
    for line in file.readlines():
        print(line[::-1])
    file.close()


reverse()
