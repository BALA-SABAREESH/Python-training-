n = int(input("Enter the number of elements: "))
arr = []
for _ in range(n):
    num = int(input("Enter a number: "))
    arr.append(num)
print("Original array:", arr)
insert_num = int(input("Enter a number to insert: "))
insert_index = int(input("Enter the index to insert at: "))
delete_index = int(input("Enter the index to delete: "))
arr.insert(insert_index, insert_num)
del arr[delete_index]
print("Array after insertion and deletion:", arr)
