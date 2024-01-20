"""
                    658. Find K Closest Elements (Medium)
-> return k(given number of) closest values to x(given number from array)
-> include smaller closest values
-> Binary Search
Time: O(logN + k) - k need to find at least k values so logN + K

"""

from typing import *


class Solution:
    def findClosest(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k  # we are searching for window not value so len(arr) - k & not len(arr) - 1

        while l < r:
            mid = (l + r) // 2  # mid: leftmost value of the window
            # arr[mid] - value in the middle
            if x - arr[mid] > arr[mid + k] - x:  # right window values are closer
                l = mid + 1
            else:
                r = mid
        return arr[l: l + k]


result = Solution()
arr = [1, 2, 3, 4, 5]  # must return [1, 2, 3, 4]
k = 4
x = 3

arr1 = [1, 2, 3, 4, 5]  # must return [1, 2, 3, 4]
k1 = 4
x1 = -1

print(result.findClosest(arr, k, x))
print(result.findClosest(arr1, k1, x1))
