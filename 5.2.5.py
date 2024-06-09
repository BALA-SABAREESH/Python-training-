n = int(input("Enter array size: "))
if n <= 1:
    print("Invalid input")
else:
    print("Enter", n, "array elements:", end=" ")
    arr = list(map(int, input().split()))
    repetitive_element = None
    for i in range(n):
        if arr[abs(arr[i])] >= 0:
            arr[abs(arr[i])] = -arr[abs(arr[i])]
        else:
            repetitive_element = abs(arr[i])
            break
    if repetitive_element:
        print("The repetitive element:", repetitive_element)
    else:
        print("Array elements are not repeated") 
