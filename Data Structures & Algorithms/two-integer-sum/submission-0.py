class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compliment = {}

        for i in range (len(nums)):
            diff = target - nums[i]
            if diff in compliment:
                return[compliment[diff], i]
            compliment[nums[i]] = i

        return [-1,-1]