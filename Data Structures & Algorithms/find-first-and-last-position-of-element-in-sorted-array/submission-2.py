class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        lb, rb = -1, -1

        while l <= r:
            mid = (l + r)//2

            if nums[mid] == target:
                r  = mid - 1
                lb = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r)//2
            if nums[mid] == target:
                l = mid + 1
                rb = mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return [lb, rb]
                
