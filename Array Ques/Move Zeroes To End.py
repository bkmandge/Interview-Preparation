# Move all zeroes to end of given list
# method 1 - partitioning the given list
"""
use 0 as a pivot swap it non-zero element.
So all the non-zero element will come at the beginning.
O(n), O(1)
"""
a = [5, 6, 0, 4, 6, 0, 9, 0, 8]

n = len(a)
j = 0
for i in range(n):
    if a[i] != 0:
        a[j], a[i] = a[i], a[j]
        j += 1
print(a)


# method 2 - sort & merge

nonZeroes = [x for x in a if x != 0]
zeroes = [y for y in a if y == 0]
arr = nonZeroes + zeroes
print(arr)
