# flip 0s with given k numbers and return max consecutive number of 1s 
# The window size can grow and shrink

from typing import List

# using brute force

def longestOnes(nums: List[int], k: int) -> int:
    n = len(nums)
    
    result = 0
    for i in range(n):
        zeroCount = 0
        for j in range(i, n):
            if nums[j] == 0:
                zeroCount += 1
            
            if zeroCount <= k:
                result = max(result, j - i + 1)
    return result

# using sliding window

def longestOnes2(nums: List[int], k: int) -> int:
    n = len(nums)

    zeroCount = 0
    left = 0
    result = 0

    for right in range(n):
        if nums[right] == 0:
            zeroCount += 1

        while zeroCount > k:
            if nums[left] == 0:
                zeroCount -= 1
            left += 1
        result = max(result, right - left + 1)
    return result

nums = [1,1,1,0,0,0,1,1,1,1,0]; k = 2   # 6 
nums2 = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]; k2 = 3  # 10

print(longestOnes(nums, k))