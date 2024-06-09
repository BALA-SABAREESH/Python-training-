a= input("Enter first string: ")
b = input("Enter second string: ")
def recursive_strcpy(src, dest, index=0):
    if index < len(src):
        dest += src[index]
        return recursive_strcpy(src, dest, index + 1)
    else:
        return dest
copied_string = ""
for char in a:
    copied_string = recursive_strcpy(char, copied_string)
print("After copying the First string:", copied_string)
print("Second string:",b)
