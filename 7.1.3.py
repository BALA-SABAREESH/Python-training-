input_string = "hello"
unique_chars = ""
for char in input_string:
    if char not in unique_chars:
        unique_chars += char
print("Original string:", input_string)
print("String with duplicates removed:", unique_chars)
