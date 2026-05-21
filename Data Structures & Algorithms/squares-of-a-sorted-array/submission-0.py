class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l, r = 0, n -1
        res = [0] * n
        idx = n - 1

        while l <= r:
            lsq = nums[l] * nums[l]
            rsq = nums[r] * nums[r]

            if lsq >= rsq:
                sq = lsq
                l += 1
            else:
                sq = rsq
                r -= 1
            
            res[idx] = sq
            idx -= 1
        
        return res