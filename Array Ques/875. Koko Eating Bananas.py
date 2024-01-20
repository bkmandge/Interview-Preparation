"""
                    875. Koko Eating Bananas (Medium)
-> return how many bananas can be eaten per hour to finish all bananas in 8 hr

"""
from typing import *
from math import ceil


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r  # default return max bananas from max piles

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:  # go through each pile
                hours += ceil(p / k)

            if hours <= h:
                res = min(res, k)
                r = k - 1  # search in left portion
            else:
                l = k + 1  # search in right portion
        return res


result = Solution()
piles = [3, 6, 7, 11]  # must return 4
h = 8

print(result.minEatingSpeed(piles, h))
