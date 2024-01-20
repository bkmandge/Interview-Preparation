"""
                    139. Single Number (Easy)
-> Find non-repeating or unique or single number from given non-empty array w/o using extra space.
-> Time: O(N), Space: O(1)
-> XOR:-  bits manipulation returns 0 result, any of num is odd returns odd num
          0 ^ 0 = 0,
          1 ^ 1 = 0,
          1 ^ 0 = 1,
          0 ^ 1 = 1

-> res = n ^ res -> converts nums to binary form & calculates bit manipulation with default res i.e. 0 & then returns result
-> 4 -> 100, 1 -> 001, 2 -> 010
"""
from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0  # num ^ 0 = num, stores default single number
        for n in nums:
            res = n ^ res
        return res


result = Solution()
list1 = [2, 2, 1]
list2 = [4, 1, 2, 1, 2]

print(result.singleNumber(list1))
print(result.singleNumber(list2))

