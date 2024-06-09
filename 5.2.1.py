array_size = int(input("Enter the array size: "))
array = []
print(f"Input {array_size} elements in an array:")
for _ in range(array_size):
    element = int(input())
    array.append(element)
unique_elements = list(set(array))
unique_elements.sort()
print("The unique elements found in the array are:", end=" ")
for element in unique_elements:
    print(element, end=" ")
