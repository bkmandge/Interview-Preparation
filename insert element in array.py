def insertAtBeginning(arr, value):
    n = len(arr)
    arr.append(0)  # add 1 space extra with 0 value to array
    
    for i in range(n, 0, -1):
        arr[i] = arr[i - 1]  # shift elements to right & then add at beginnig
    arr[0] = value
    print(arr)


        
arr = [1,2,3,4,5]
print(arr)

# arr.insert(0, 0)
# print(arr)


insertAtBeginning(arr, value = 100)