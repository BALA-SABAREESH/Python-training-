str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
count = [0] * 256
for char in str2:
    count[ord(char)] += 1
for char in str1:
    count[ord(char)] -= 1
for i in range(256):
    if count[i] != 0:
        extra_char = chr(i)
        break
print("The extra character is:", extra_char)
