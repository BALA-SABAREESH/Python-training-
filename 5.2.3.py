num = int(input("Enter how many values you want to read: "))
array = [] 
for i in range(num):
    value = int(input(f"Enter the value of a[{i}]: "))
    array.append(value)
sums = sum(array)
print(f"The sum of array elements = {sums}")
