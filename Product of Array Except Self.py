"""
                    Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


"""


def product_Except_Self(nums):
    # to store product of all numbers in result array
    res = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        res[i] = prefix
        prefix = prefix * nums[i]

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        res[i] = res[i] * postfix
        postfix = postfix * nums[i]

    return res
