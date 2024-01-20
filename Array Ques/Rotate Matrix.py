"""

WAP to rotate the given image by 90 degrees. w/o using extra space

Time complexity:- O(n2)
Space complexity:- O(1)

algo:-

for i = 0 to n:
    temp = top[i]
    top[i] = left[i]
    left[i] = bottom[i]
    bottom[i] = right[i]
    right[i] = temp

"""
import numpy as np

myArray = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(myArray)


def rotateMatrix(matrix):
    # to get no. of rows
    n = len(matrix)
    for layer in range(n // 2):
        first = layer
        last = n - layer - 1

        for i in range(first, last):
            # save top element
            top = matrix[layer][i]

            matrix[layer][i] = matrix[-i -1][layer]

            matrix[-i - 1][layer] = matrix[- layer - 1][- i - 1]

            matrix[- layer - 1][- i - 1] = matrix[i][- layer - 1]

            matrix[i][- layer - 1] = top
    return matrix


print(rotateMatrix(myArray))


'''
another way:


'''
'''
left & right boundaries r = column - 1
'''
def rotate(matrix):
    l, r = 0, len(matrix) - 1
    while l < r:
        for i in range(r - l):
            top, bottom = l, r
            # add +i to top & top[l] to move to next element
            topLeft = matrix[top][l + i]
            # minus -i from bottom & bottom[r] to move to upper element
            matrix[top][l + i] = matrix[bottom - i][l]
            matrix[bottom - i][l ] = matrix[bottom][r - i]
            matrix[bottom][r - i] = matrix[top + i][r]
            matrix[top + i][r] = topLeft

        # to go to next layer
        r -= 1
        l += 1

        return matrix


print(rotate(myArray))
