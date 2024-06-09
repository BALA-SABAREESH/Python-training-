str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if str1 == str2:
    print(f"{str1} is equal to {str2}")
else:
    if len(str1) == len(str2):
        print(f"{str1} is not equal to {str2}, but they have equal lengths")
    elif len(str1) > len(str2):
        print(f"{str1} is not equal to {str2}, {str1} is greater than {str2}")
    else:
        print(f"{str1} is not equal to {str2}, {str1} is less than {str2}") 
