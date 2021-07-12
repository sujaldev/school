# 10)WAF to find and display the occurrence of the word ‘we’ in text file ‘poem.txt’.

def we_count():
    file = open("poem.txt")
    count = file.read().replace("\n", " ").split(" ").count("we")
    print(f"There are {count} occurrences of the word we in poem.txt")
    file.close()


we_count()
