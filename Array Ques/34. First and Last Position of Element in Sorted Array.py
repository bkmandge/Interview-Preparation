'''
                    34. First and Last Position of Element in Sorted Array (Medium)

-> return starting & ending index of given target value. If not found return [-1, -1]

Binary Search -> call twice as need two indices - right most & left most
        implement regular binary search
        even we found result, at the end do check again:-
                if leftBias:  # looking for left most index
                    r = mid - 1
                else:  # looking for right most index
                    l = mid + 1


Time: O(logN)
Space: O(logN)

'''

from typing import *


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        return [left, right]  # return left most & right most indices

    # leftBias = [True/False], if False res is rightBiased
    def binSearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1  # if not found return -1

        while l <= r:
            mid = (l + r) // 2
            if target > nums[mid]:
                l = mid + 1
            elif target < nums[mid]:
                r = mid - 1
            else:
                i = mid
                if leftBias:  # looking for left most index
                    r = mid - 1
                else:  # looking for right most index
                    l = mid + 1
        return i


result = Solution()

nums = [5, 7, 7, 8, 8, 10]  # [3, 4]
nums2 = [5, 7, 7, 8, 8, 10]  # [-1, -1]

print(result.searchRange(nums, 8))
print(result.searchRange(nums2, 6))
