class Solution:
    def maxProfit(self, p: List[int]) -> int:
        buy = 0
        sell = 1

        max_profit = 0

        while sell < len(p):

            max_profit = max(max_profit, p[sell] - p[buy])

            buy = sell if p[sell] < p[buy] else buy

            sell += 1
        
        return max_profit

            