'''
                    209. Minimum Size Subarray Sum (Medium)

-> Return minimum smallest size of contiguous subarray which contains sum of given target
Time: O(N) - need to go through entire list
Space: O(1) - only two pointers

'''

from typing import *


class Solution:
    def minSizeArray(self, nums: List[int], target: int) -> List[int]:
        l, total = 0, 0
        res = float("inf")

        for r in range(len(nums)):  # incrementing right pointer each time & adding its val to total
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)  # calculating size of window
                total -= nums[l]
                l += 1

        if res == float("inf"):  # if big value than len(nums) return 0 as no such val
            return 0
        else:
            return res


result = Solution()
nums = [2, 3, 1, 2, 4, 3]
nums2 = [1, 4, 4]

print(result.minSizeArray(nums, 7))
print(result.minSizeArray(nums2, 4))

