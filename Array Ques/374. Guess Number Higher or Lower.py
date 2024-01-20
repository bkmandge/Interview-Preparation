'''
                        374. Guess Number Higher or Lower (Easy)
-> Guessing game
-> Binary Search
Time: O(logN)
Space: O(1)
'''

from typing import *


class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while True:
            mid = (l + r) // 2
            res = guess(mid)  # already pre-defined guess() on leetcode
            if res > 0:
                l = mid + 1
            elif res < 0:
                r = mid - 1
            else:
                return mid


result = Solution()
print(result.guessNumber(10))
