"""
I/P:-
nums1 = [1, 2, 3, 0, 0, 0] # here 0s are empty spaces.
nums2 = [2, 5, 6]

O/P:- [1, 2, 2, 3, 5, 6]

"""
from typing import *

# m & n are last values' indices of nums1 & nums2 lists
def merge(nums1:List[int], m:int, nums2:List[int], n:int) -> None:
    # Last index of nums1 i.e. length
    a = m - 1
    b = n - 1
    last = m + n - 1

    # merge in reverse order, decrement m & n pointers as doing in reverse order
    while m > 0 and n > 0:
        if nums1[a] > nums2[b]:
            # index starts from 0 so, m -1 & n -1
            nums1[last] = nums1[a]
            m -= 1
        else:
            n = 1
        last -= 1

    # fill nums 1 with leftover of nums2 elements
    while n > 0:
        nums1[last] = nums2[b]
        n, last = n - 1, last - 1


nums1 = [1, 2, 3, 0, 0, 0]  # here 0s are empty spaces.
nums2 = [2, 5, 6]
size = len(nums1)
size1 = len(nums2)
print(merge(nums1, size, nums2, size1))



