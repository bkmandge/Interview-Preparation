"""
                11. Container With Most Water (Medium)
Given array of heights.
-> find the biggest area we can form with the container that has left & right heights


finding the height:- min(height[l], height[r]) -> bottle neck (i.e. 1)- min height from where water will spill off from the container
area of rectangle formula = width * height
                : (r - l) * min(height[l], height[r])
                : r - l -> to find width
                : min(height[l], height[r]) -> to get the height

"""

from typing import *


class Solution:
    def maxArea(self, height: List[int]) -> int:
        # two pointer technique - O(n)
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res


result = Solution()
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(result.maxArea(height))



'''
Brute Force O(n2) -> time exceeds
        res = 0
        for l in range(len(height)):
            for r in range(l + 1, len(height)):
                area = (r - l) * min(height[l], height[r])
                res = max(res, area)

        return res


'''