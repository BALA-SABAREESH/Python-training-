a = input("Enter the first string: ")
b = input("Enter the second string: ")
print("Length of first string:", len(a))
print("Length of second string:", len(b))
print("Copy of first string:", a)
cancat = a + b
print("Concatenation of both strings:", concat)
print("Uppercase of first string:", a.upper())
if a < b:
    print("First string is alphabetically before second string")
elif a > b:
    print("Second string is alphabetically before first string")
else:
    print("Both strings are equal")
s = "Hello, World!"
c = 'l'
index = -1
for i, char in enumerate(s):
    if char == c:
        index = i
if index != -1:
    last_occurrence = s[index:]
else:
    last_occurrence = None
print("Last occurrence of 'l':", last_occurrence)
