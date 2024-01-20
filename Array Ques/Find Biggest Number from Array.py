''''
1. Iterative way -
            1. assign first num as big number & iterate through rest of given array,
            2. compare with first number & asssign it to big number if it is
            3. return big number
2. Recursive way -
            1. if num == 1: return array[0]
            2. check max of array[n - 1], recursive call array, n - 1
                i.e. max(array1[n-1], findMaxNumRec(array1, n-1))

'''

customArray = [1,10,45,33,23,45,67,2,3,33,55,11,65,76,34,35,27,99]

def findBiggestNumber(array):
    biggestNumber = array[0]
    for i in range(1, len(array)):
        if array[i] > biggestNumber:
            biggestNumber = array[i]
    return biggestNumber


# print(findBiggestNumber(customArray))


def findMaxNumRec(array1, n):
    if n == 1:
        return array1[0]
    return max(array1[n-1], findMaxNumRec(array1, n-1))


print(findMaxNumRec(customArray, len(customArray)))
