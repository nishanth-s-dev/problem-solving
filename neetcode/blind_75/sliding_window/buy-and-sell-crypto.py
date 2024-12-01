# https://neetcode.io/problems/buy-and-sell-crypto

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices) - 1):
            for j in range(i + 1, len(prices)):
                current_profit = prices[j] - prices[i]
                profit = max(current_profit, profit)

        return profit

    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = float("inf")

        for price in prices:
            min_price = min(price, min_price)
            profit = max(profit, price - min_price)

        return profit