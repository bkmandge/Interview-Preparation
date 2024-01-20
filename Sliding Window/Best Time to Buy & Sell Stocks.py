"""
Space complexity:- O(1) -> just creating two pointers so not req extra spaces
Time complexity:- O(n) -> linear as we are not doing any brute force, need to scan array once only

1. define two pointers # left = date of buy, right = date of sell & maxProfit = 0
2. loop while selling pointer has not passed end of price list
3. check if its profitable, i.e. buying @ less cost & selling @ high cost -> calculate profit (sell - buy)
4. & max(maxP, profit)
5. else assign left = right to buy next lowest price stock
6. increase right by 1 to check entire price list for profit
7. return maxProfit

"""

from typing import *


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            # profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r  # left= buying price should be less than right=selling price
            r += 1
        return maxP


ans = Solution()
print(ans.maxProfit([7, 1, 5, 3, 6, 4]))
