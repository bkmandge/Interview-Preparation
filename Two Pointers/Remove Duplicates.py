"""
                            Remove Duplicates
Given non-decreasing order of array i.e. increasing or sorted ascending array, remove duplicates w/o using extra mem.
(in place sorting is asked)

O(n):- Using two pointers and scanning through
This is linear solution so, no extra mem is required.

I/P:- [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
O/P:- 5 = [0, 1, 2, 3, 4]

Using right pointer:- to scan through array
      left pointer:- to tell us where to place next unique value & how many unique values we have so far
                  :- gives us o/p parameter i.e. 5

1. declare l = 1 counter pointer as first element will be unique in the beginning
2. loop r pointer in given list
3. check if r != r -1
        if not then assign it to l & increase l's count by 1
4. return l counter pointer

"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l


ans = Solution()
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(nums)
print(ans.removeDuplicates(nums))

