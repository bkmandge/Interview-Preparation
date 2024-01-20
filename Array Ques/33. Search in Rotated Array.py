'''
                33. Search in Rotated Array (Medium)
                
-> Return index of value if present else return -1.

I/P: nums = [4, 5, 6, 7, 0, 1, 2], target = 0
O/P: 4

-> Binary Search -> Two halves are sorted, left, mid & right pointers used
-> Time & space: O(logN)
'''

from typing import *


class Solution:
    def searchinRotatedArray(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        # [1] -> to check if only one value given in the list so, l <= r
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            # right sorted portion
            else:
                if target < nums[mid]:
                    r = mid - 1
                elif target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


result = Solution()
nums = [4, 5, 6, 7, 0, 1, 2]

print(result.searchinRotatedArray(nums, 0))
print(result.searchinRotatedArray(nums, 10))
