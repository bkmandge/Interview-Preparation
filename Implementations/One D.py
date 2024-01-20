'''

Need to import array module
Array operations:- Traversal, Insert, Append, Index, Search -> value, Remove

'''
import array as arr

oneDArray = arr.array('i', [10, 20, 30, 40])
print(oneDArray)

# Traversing
def traverseArray(array):
    for i in range(len(array)):
        print(array[i])

print(traverseArray(oneDArray))


# Insertion
oneDArray.insert(0, 0)
print(oneDArray)

# Append at the end
oneDArray.append(100)
print(oneDArray)


# Deletion
oneDArray.remove(100)
print(oneDArray)

# Finding index
print(oneDArray.index(20))

# Searching
def searchElement(array, value):
    for i in range(len(array)):
        if array[i] == value:
            print("Found at index:", i)

searchElement(oneDArray, 10)
