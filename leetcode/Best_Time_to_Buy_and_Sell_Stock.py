class Solution:
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        max_profit = 0
        min_price = prices[0]
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) == 1:
            return 0
        max_profit = 0
        min_price = max_price = prices[0]
        for current_price in prices[1:]:
            if current_price < min_price:
                min_price = max_price = current_price
            elif current_price > max_price:
                max_price = current_price
            current_profit = max_price - min_price
            max_profit = max(max_profit, current_profit)
        return max_profit
