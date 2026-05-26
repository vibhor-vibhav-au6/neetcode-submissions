class Solution:
    def maxProfit(self, p: List[int]) -> int:
        buy = 0
        mp = 0

        for sell in range (1, len(p)):
            mp = max(mp, p[sell] - p[buy])

            buy = sell if p[sell] < p[buy] else buy

        return mp