class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []

        for i in range (len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            t = 0 - nums[i]
            l = i+1
            r = len(nums) - 1

            while l < r:
                tsum = nums[l] + nums[r]
                if tsum  == t:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1

                elif tsum > t:
                    r -= 1
                else:
                    l += 1
            
        return res

            
        