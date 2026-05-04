class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()

        l = 0
        r = len(nums) - 1

        res = -1

        while l < r:
            s = nums[l] + nums[r]
            if s < k:
                res = max(res, s)
                l += 1
            elif s >= k:
                r -= 1
        
        return res



        