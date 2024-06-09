a= input("Enter the first string: ")
b = input("Enter the second string: ")
print("Length of first string:", len(a))
print("Length of second string:", len(b))
print("Copy of first string:", a)
concat_string = a + b
print("Concatenation of both strings:", concat_string)
print("Uppercase of first string:", a.upper())
if a < b:
    print("First string is alphabetically before second string")
elif a > b:
    print("Second string is alphabetically before first string")
else:
    print("Both strings are equal")
