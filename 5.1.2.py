array = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
element = int(input("Enter the element to search for: "))
position = -1  
for i in range(len(array)):
    if array[i] == element:
        position = i
        break
if position != -1:
    print(f"Element {element} found at position {position}.")
else:
    print(f"Element {element} not found in the array.")
