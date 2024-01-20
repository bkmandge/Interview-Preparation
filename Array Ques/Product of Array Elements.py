def productofArray(arr):
    if len(arr) == 0:
        return 1
    return arr[0] * productofArray(arr[1:])


arr = [1, 2, 3]
print(productofArray(arr))

