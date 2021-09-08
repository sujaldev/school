"""
WAP to input a string, capitalize every alternate character in a string
E.g: original string : computer science
 new string after alternate character in upper : cOmPuTeR ScIeNcE
"""
char_list = list(input("Enter a string: "))

for i in range(1, len(char_list), 2):
    char_list[i - 1] = char_list[i - 1].lower()
    char_list[i] = char_list[i].upper()

print("Alternate Case: ")
print("".join(char_list))
