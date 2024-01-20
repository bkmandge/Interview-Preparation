'''
                    410. Split Array Largest Sum (Hard)
-> Return continuous subarray (m) containing max sum
-> Binary Search
Time:- n.logS - S is the sum of input array, n - need to split the entire array into sub groups


1. create two boundaries:-
    l = max(nums) - smallest result we can return
    r = sum(nums) - max result we can return
2. initially return res as max from left & right boundaries
    res = r
3. compute mid
'''

from typing import *


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def canSplit(largest):
            subArray = 0
            curSum = 0
            for n in nums:
                curSum += n
                if curSum > largest:
                    subArray += 1
                    curSum = n
            return subArray + 1 <= m

        l, r = max(nums), sum(nums)
        res = r

        while l <= r:
            mid = (l + r) // 2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1


result = Solution()
nums = [7, 2, 5, 10, 8]  # must return 18 i.e. [10, 8]
m = 2

result.splitArray(nums, m)
