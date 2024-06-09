n = int(input("Enter how many values you want to read: "))
values = []
for i in range(n):
    value = int(input(f"Enter value {i+1}: "))
    values.append(value)
values.sort()
print("Sorted array in ascending order:")
for value in values:
    print(value)
