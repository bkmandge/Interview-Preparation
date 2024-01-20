"""
                   448. Find All Numbers Disappeared in an Array (Easy)
-> find disappeared numbers in the range(1, n)

I/P: nums = [4, 3, 2, 7, 8, 2, 3, 1]
O/P: [5, 6]

-> In-place
1. Go through every element, mark the disappeared numbers -
    get index of those numbers
2. Check numbers > 0 are missing numbers & append their indices to result
3. return result
"""

from typing import *


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for n in nums:
            i = abs(n) - 1  # getting new indices
            nums[i] = -1 * abs(nums[i])  # mapping to existing indices

        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        return res


result = Solution()
list1 = [4, 3, 2, 7, 8, 2, 3, 1]

print(result.findDisappearedNumbers(list1))

