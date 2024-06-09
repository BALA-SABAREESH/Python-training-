num_list = []
num_count = int(input("Enter the number of elements: "))
for i in range(num_count):
    num = float(input("Enter number {}: ".format(i + 1)))
    num_list.append(num)
if num_list:
    largest = num_list[0]
    smallest = num_list[0]
    for num in num_list:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num
    print("Largest number:", largest)
    print("Smallest number:", smallest)
else:
    print("No numbers provided.").
