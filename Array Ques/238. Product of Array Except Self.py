"""
                    238. Product of Array Except Self (Medium)

-> Get product of other array nums except the self
-> Constraint:- O(n) time w/o using division operation

I/P: nums = [1, 2, 3, 4]
O/P: [24, 12, 8, 6]
    i.e. [2*3*4, 3*4*1, 4*2*1, 1*2*3 ]

1. create result o/p array, assign default value of 1 to all array size
2. create 2 passes
    1. prefix - starting from 0 to end.
                prefix = 1 -> to compute prefix of 1st element of array
    2. postfix starting from end to 0 product counting
                postfix = 1 -> to compute postfix of last element of array
                res[i] *= postfix -> multiplying previously stored prefix values with postfix to get result

"""

from typing import *


class Solution:
    def productOfArrayExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix                 # 1, 1, 2, 6
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res


ans = Solution()

print(ans.productOfArrayExceptSelf([1, 2, 3, 4]))
