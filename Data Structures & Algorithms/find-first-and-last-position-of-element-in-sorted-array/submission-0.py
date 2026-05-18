class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
            

        while l <= r:
            mid = (l + r)//2

            if nums[mid] == target:
                # do something
                lb = mid
                rb = mid
                while lb >= 0 and nums[lb] == target:
                    lb -= 1
                while rb < len(nums) and nums[rb] == target:
                    rb += 1

                return [lb + 1, rb - 1]
                
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return [-1, -1]