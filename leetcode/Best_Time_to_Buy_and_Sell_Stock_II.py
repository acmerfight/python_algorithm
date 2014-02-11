#Say you have an array for which the ith element is the price of a given stock on day i.
#
#Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).

class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        sum_profit = 0
        if len(prices) == 1:
            return sum_profit
        for index, price in enumerate(prices[1:]):
            diff = price - prices[index]
            if diff > 0:
                sum_profit += diff 
        return sum_profit
                            
