"""
            1423. Max points You Can Obtain from Cards (Medium)

"""

from typing import *


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l, r = 0, len(cardPoints) - k
        total = sum(cardPoints[r:])  # stores last 3 elements' sum
        res = total

        while r < len(cardPoints):
            total += cardPoints[l] - cardPoints[r]
            res = max(res, total)
            l += 1
            r += 1
        return res


result = Solution()
cardPoints = [1, 2, 3, 4, 5, 6, 1]
k = 3

print(result.maxScore(cardPoints, k))
