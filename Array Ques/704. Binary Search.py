'''
                    704. Binary Search (Easy)

-> return index of number if it exists else return -1.
-> Binary Search
Time: O(logN)
'''
from typing import *


class Solution:
    def binarySearch(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid
        return -1


result = Solution()

nums = [-1, 0, 3, 5, 9, 12]  # as 9 exists in nums & its index is 4
target = 9

nums2 = [-1, 0, 3, 5, 9, 12]  # as 2 does not exist in nums2 so return -1
target2 = 2

print(result.binarySearch(nums, target))
print(result.binarySearch(nums2, target2))
