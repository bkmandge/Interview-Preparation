"""
                189. Rotate Array (Medium)
-> Rotate the array to the right by K steps, where K is non-negative. (Medium)

I/P: nums = [1, 2, 3, 4, 5, 6, 7], k = 3
O/P: [5, 6, 7, 1, 2, 3, 4]

rotate 1 steps to the right = [7, 1, 2, 3, 4, 5, 6]
rotate 2 steps to the right = [6, 7, 1, 2, 3, 4, 5]
rotate 3 steps to the right = [5, 6, 7, 1, 2, 3, 4]
s
-> Time O(N), Space O(1) - in- place reversing done
->
"""

from typing import *


def rotate(nums: List[int], k: int) -> List[int]:
    k = k % len(nums)  # k = means rotation steps, k must not be greater than given array so..
    l, r = 0, len(nums) - 1  # pointers

    # first reversing entire array by swapping elements in-place
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1  # increment & decrease pointers

    # reversing k-1 array
    l, r = 0, k - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

    # reversing remaining array, from k to end of array
    l, r = k, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

    return nums


nums = [1, 2, 3, 4, 5, 6, 7]
print(rotate(nums, 3))


