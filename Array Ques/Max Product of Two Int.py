'''

WAP to find max product of two integers in the array where all elements are positive.

Time Complexity: O(n2)

1. declare maxProduct = 0
2. loop through given array twice
3. check if array[i] * array[j] > maxProduct then assign these values to maxProduct
4. & also assign to pairs variable
5. finally print pairs & maxProduct

'''

myArray = ([1, 20, 30, 44, 5, 56, 57, 8, 9, 10, 31, 12, 13, 14, 35, 16, 27, 58, 19, 21])


def findMaxProduct(array):
    maxProduct = 0
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if array[i] * array[j] > maxProduct:
                maxProduct = array[i] * array[j]
                pairs = str(array[i]) + "," + str(array[j])
    print(pairs)
    print(maxProduct)


findMaxProduct(myArray)
