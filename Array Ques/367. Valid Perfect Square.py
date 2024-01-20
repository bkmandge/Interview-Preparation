"""
                    367. Valid Perfect Square (Easy)

-> Return True if number is perfect square else return False
-> Don't use built-in functions such as sqrt
-> 1 = 1(is a perfect square), 2 = 4(is a perfect square)
-> Binary Search
"""

from typing import *


class Solution:
    def validPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l <= r:
            mid = (l + r) // 2
            if mid * mid > num:
                r = mid - 1
            elif mid * mid < num:
                l = mid + 1
            else:
                return True
        return False


result = Solution()
print(result.validPerfectSquare(16))  # must return True
print(result.validPerfectSquare(14))  # must return False
