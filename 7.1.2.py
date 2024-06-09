string = input("Enter the string: ")
a = input("Enter the character to replace: ")
b = input("Enter the replacement character: ")
index = -1
for i in range(len(string)):
    if string[i] == a:
        index = i
        break
if index != -1:
    string = string[:index] + b + string[index + 1:]
print("Resultant string:", string)
