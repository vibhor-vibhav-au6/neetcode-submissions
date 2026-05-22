class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        res = r
        s = 0

        while l <= r:
            mid = (l + r) // 2
            s = 0
            for p in piles:
                s += math.ceil(p/mid)
            
            if s <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return res


        