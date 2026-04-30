class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_idx = 0
        sell_idx = 1

        max_p = 0

        while sell_idx < len(prices):
            if prices[sell_idx] - prices[buy_idx] > max_p:
                max_p = prices[sell_idx] - prices[buy_idx]
            
            if prices[sell_idx] < prices[buy_idx]:
                buy_idx = sell_idx
            sell_idx += 1
        
        return max_p