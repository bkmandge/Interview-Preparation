'''

                    441. Arranging Coins (Easy)
-> Build a staircase with given coins & return complete rows of the staircases
-> given 5 coins -> o/p: 2 staircases
1st row - 1 coin
2nd row - 2 coins
3rd row - 3 coins

'''
from typing import *


class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 1, n
        res = 0

        while l <= r:
            mid = (l + r) // 2  # here mid is row
            coins = (mid / 2) * (mid + 1)
            if coins > n:  # coins > we have i.e. n
                r = mid - 1
            else:
                l = mid + 1
                res = max(mid, res)
        return res


result = Solution()
print(result.arrangeCoins(5))  # must return 2


