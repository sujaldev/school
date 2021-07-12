# 3)Write a function to count and display number of words which
# starts with alphabet a in an existing text file 'story.txt'.


def count_a():
    file = open("story.txt")
    count = 0
    for word in file.read().split(" "):
        if word.startswith("a"):
            count += 1
    print(f"There are {count} words which start with a.")
    file.close()


count_a()
