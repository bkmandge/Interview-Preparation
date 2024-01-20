"""
                            Concatenation of Array

Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
Return the array ans.

Input: nums = [1,2,1]
Output: [1,2,1,1,2,1]
Explanation: The array ans is formed as follows:
- ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
- ans = [1,2,1,1,2,1]

Input: nums = [1,3,2,1]
Output: [1,3,2,1,1,3,2,1]

"""


def getConcatenation(nums):
    return nums * 2


nums = [1,3,2,1]
print(getConcatenation(nums))