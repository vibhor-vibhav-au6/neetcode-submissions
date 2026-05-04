class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet = set(nums)

        res = 0

        for i in range(0, len(nums)):
            sub_len = 0
            # start of a sequence
            if nums[i-1] + 1 != nums[i]:
                sub_len = 0
                while (nums[i] + sub_len) in numSet:
                    sub_len += 1

            res = max(res, sub_len) 

        return res

