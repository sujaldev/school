# 11)WAF to read the text from file ‘poem.txt’ and
# replace the occurrence of ‘that’ with ‘this’ and
# store the entire file content after replacement in file ‘ufile.txt’.

def replace_that():
    file, new_file = open("poem.txt"), open("ufile.txt", "w")
    new_file.write(file.read().replace("that", "this"))
    file.close()
    new_file.close()


replace_that()
