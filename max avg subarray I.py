from typing import List

# Brute force approach
def findMaxAverage(nums: List[int], k: int) -> float:
    n = len(nums)
    maxAvg = float("-inf")
    
    # iterate through all possible subarrays of k size
    # calculate current window total and average
    # and then update maxAvg
    for i in range(n - k + 1):
        total = sum(nums[i: i+k])
        currAvg = total / k
        maxAvg = max(maxAvg, currAvg)
    return maxAvg


# Sliding window approach
def findMaxAverage2(nums: List[int], k: int) -> float:
    n = len(nums)
    maxAvg = float("-inf")
    total = 0

    for i in range(n):
        total += nums[i]

        # If the current index is beyond the sliding window size
        # update maxAvg
        # subtract left most val
        if i >= k - 1:
            maxAvg = max(maxAvg, total / k)
            total = total - nums[i - k + 1]     
    return maxAvg


nums = [1,12,-5,-6,50,3]; k = 4     # 12.75000
nums2 = [5]; k2 = 1     # 5.0000

print(findMaxAverage(nums, k))