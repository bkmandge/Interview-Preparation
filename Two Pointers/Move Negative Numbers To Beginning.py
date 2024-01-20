"""
                    Move all negative numbers to beginning and positive to end with constant extra space
Two Pointer Approach: O(n), O(1) - in-place re-arrangement so extra space taken.

1. Check If the left and right pointer elements are negative then simply increment the left pointer.
Otherwise, if the left element is positive and the right element is negative then simply swap the elements,
            and simultaneously increment and decrement the left and right pointers.
Else if the left element is positive and the right element is also positive then simply decrement the right pointer.
Repeat the above 3 steps until the left pointer ? right pointer.

"""


def shiftAll(arr, l, r):
    while l < r:
        if arr[l] < 0 and arr[r] < 0:
            l += 1
        elif arr[l] > 0 > arr[r]:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        elif arr[l] > 0 and arr[r] > 0:
            r -= 1
        else:
            l += 1
            r -= 1
    return arr


arr = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
arr2 = [-12, 11, -13, -5, 6, -7, 5, -3, 11]
n = len(arr2)
print(shiftAll(arr2, 0, n - 1))
