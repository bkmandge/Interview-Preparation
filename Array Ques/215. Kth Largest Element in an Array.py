"""
                    215. Kth Largest Element in an Array (Medium)

-> return Kth largest element. K = steps from last value
-> Quick Select:- with pivot element searches in either half of array each time

Time: O(N)
Space: O(N)

# Easiest way:
        nums.sort()
        return nums[len(nums) - k]

# Another way - Quick Select
1. assign pivot = right most value, p pointer = left most index
2. iterate through entire list
    if nums[i] <= pivotValue: swap left most value nums[p] with nums[i]
    increment p pointer by 1
3. swap pivot value with right most value nums[p], nums[r] = nums[r], nums[p]
4. if k is smaller than p pointer do quick select on left side
    else do quick select on right side

"""

from typing import *


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(l, r):
            # Partition
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            # swap the pivot value with p index
            nums[p], nums[r] = nums[r], nums[p]

            if p > k:
                return quickSelect(l, p - 1)  # look in left partition array
            elif p < k:
                return quickSelect(p + 1, r)
            else:
                return nums[p]

        return quickSelect(0, len(nums) -1)


result = Solution()
nums = [3, 2, 1, 5, 6, 4]  # should return 5
nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]  # should return 3

print(result.findKthLargest(nums, 2))
print(result.findKthLargest(nums2, 6))
