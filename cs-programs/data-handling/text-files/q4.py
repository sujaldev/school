# 4)WAF to display the number of lines in the file ‘story.txt’.


def count_lines():
    file = open("story.txt")
    print(f"There are {len(file.readlines())} lines in the file story.txt")
    file.close()


count_lines()
