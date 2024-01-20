'''
                153. Find Minimum in Rotated Sorted Array (Medium)
-> Find min value in O(logN) time.
-> Array sorted in ascending order but also ROTATED between 1 & n times.

[0, 1, 2, 4, 5, 6, 7] -> 7 times rotated
[4, 5, 6, 7, 0, 1, 2] -> 4 times rotated

-> Binary Search
nums[mid] >= nums[left]: search in right side
                   else: search in left side

'''

from typing import *


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1

        # if sorted sub-array rec'd in given array, returns min value easily
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            # else do binary search
            mid = l + r // 2
            res = min(res, nums[mid])

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return res


result = Solution()
nums = [3, 4, 5, 1, 2]
print(result.findMin(nums))
