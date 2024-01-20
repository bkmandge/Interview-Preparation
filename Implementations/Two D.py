"""
Traversing:- for row elements:- len(array), column:- len(array[0])

Insertion:- Row axis = 0, Column axis = 1

"""
import numpy as np

twoDArray = np.array([[1, 2, 3], [10, 20, 30], [100, 200, 300]])

# Insertion
# newDArray = np.insert(twoDArray, 0, [0, 0, 0], axis=1)

# Append
newDArray = np.append(twoDArray, [[11, 22, 33]], axis=0)


print(twoDArray)
# print(newDArray)

print(f'Rows are {len(newDArray)}')
print(f'Columns are {len(twoDArray[0])}')


# Accessing element:- check if provided index is in range

def accessElement(array, row_index, col_index):
    if row_index >= len(array) or col_index >= len(array[0]):
        print('Index out of range!')
    else:
        print(array[row_index][col_index])


# accessElement(twoDArray, 5, 2)


# Traversing array:- row by row, in each row visiting first column, second column n so on...
def traverseTArray(array):
    print('Traversing two dimensional array')
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])


# traverseTArray(newDArray)


# Searching element:-
def searchElement(array, searchValue):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == searchValue:
                return 'Found search value at row index '+str(i)+" and column index "+str(j)
    return 'No such value in array!'


# print(searchElement(twoDArray, 1000))


# Deleting row / column:- creates new array in memory
newArray = np.delete(twoDArray, 1, axis=1)
print(newArray)
