'''
                        35. Search Insert Position (Easy)

-> Return index of target if found in given sorted array.
If not found return where it would be if it were inserted in order.

-> Binary Search
Time: O(logN)

'''

from typing import *


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        # if [2] single value given & l, r pointing to same then only l pointer need to shift to either left or to right
        return l


result = Solution()
nums = [1, 3, 5, 6]  # index 2
target = 5

nums1 = [1, 3, 5, 6]  # index 1
target1 = 2

nums2 = [1, 3, 5, 6]  # index 4
target2 = 7

print(result.searchInsert(nums, target))
print(result.searchInsert(nums1, target1))
print(result.searchInsert(nums2, target2))