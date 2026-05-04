class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        nums.sort()
        res = 1
        sub_len = 1
        if not nums:
            return 0
        for i in range (1, len(nums)):
            if nums[i] == nums[i-1]:
                continue
            if nums[i] == nums[i-1] + 1:
                sub_len += 1
            else:
                sub_len = 1
            res = max(res, sub_len)

        return res
