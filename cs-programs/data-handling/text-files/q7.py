# 7)WAF to read a text file and display the count of vowels and consonants in the file ‘poem.txt’.

def grammar():
    file = open("poem.txt")
    data = file.read().replace("\n", "").replace(" ", "")
    l = ["v" if char.lower() in "aeiou" else "c" for char in data]
    vowel_count, const_count = l.count("v"), l.count("c")
    print(f"Vowel Count = {vowel_count} and Consonant Count = {const_count}")
    file.close()


grammar()
