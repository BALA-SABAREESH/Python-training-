num = int(input("Enter how many values you want to read: "))
a = []
b = []
for i in range(num):
    value = int(input(f"Enter the value of a[{i}]: "))
    a.append(value)
for i in range(num):
    value = int(input(f"Enter the value of b[{i}]: "))
    b.append(value)
if a == b:
    print("Both arrays are equal")
else:
    print("Both arrays are not equal")
