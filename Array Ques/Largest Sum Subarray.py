"""
                        Largest Sum Subarray
-> Return contiguous sub-array which has the largest sum (sub-array should contain at least one number )


I/P:- [-2, 1, -3, 4, -1, 2, 1, -5, 4]
O/P:- largest sum 6
Sub-array = [4, -1, 2, 1]

*Using linear time algo O(n), no need of extra memory
*removing negative prefixes portion if curSum < 0 from given array each time seems as sliding window

1. create maxSub var & assign first value to this sub array, to start comparison between maxSub & curSum
2. create curSum - to calculate constantly through the array
3. loop through given array
    check if curSum < 0 & remove negative prefixes portion & reset curSum = 0
    else add num to curSUm
    check max of maxSub & curSum & return maxSub

"""
from typing import *


def maxSubArray(nums: List[int]) -> int:
    maxSub = nums[0]
    curSum = 0

    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSum)
    return maxSub


customArray = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(customArray))
