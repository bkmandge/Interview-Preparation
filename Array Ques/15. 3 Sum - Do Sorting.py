"""
                    15. 3 Sum (Medium)
-> return list of array containing 3 elements which returns value of 0 after their total.

Time: O(N2)
    O(NLogN) -> sorting given array + nested loop for two sum O(N2) = O(N2)
SPace: O(N) -> extra space req for sorting
"""
from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []  # result list to be returned
        nums.sort()

        for i, v in enumerate(nums):
            if i > 0 and v == nums[i - 1]:  # v starts from 0th index element
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = v + nums[l] + nums[r]  # l stores second value & r stores end value
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([v, nums[l], nums[r]])
                    l += 1
                    # to skip if first & second number are same [-1, -1, 0, 0, 2, 2]
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


result = Solution()
list1 = [-1, 0, 1, 2, -1, -4]
print(result.threeSum(list1))
