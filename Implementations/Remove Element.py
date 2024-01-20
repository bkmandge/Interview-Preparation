'''

1. Loop through given array, check if given array element != given value,
2. then swap it with array[counter] = array[i] & increment counter by 1

'''
nums = [0, 1, 2, 2, 3, 0, 4, 2]

def removeElement(array, value):
    k = 0 #counter variable

    for i in range(len(array)):
        if array[i] != value:
            array[k] = array[i]
            k += 1
    return k


print(removeElement(nums, 2))
