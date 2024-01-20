'''
                    977. Squares of a Sorted Array (Easy)

-> return squares of each array value in sorted order.
Time & Space: O(N)
'''

from typing import *


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = []
        l, r = 0, len(nums) -1

        while l <= r:
            if nums[l] * nums[l] > nums[r] * nums[r]:
                res.append(nums[l] * nums[l])
                l += 1
            else:
                res.append(nums[r] * nums[r])
                r -= 1

        return res[::-1]  # reverse


result = Solution()
nums = [-4, -1, 0, 3, 10]

print(result.sortedSquares(nums))
