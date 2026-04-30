class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 999
        max_profit = 0

        for i in range (len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            
            if max_profit < prices[i] - min_price:
                max_profit = prices[i] - min_price
            
        return max_profit