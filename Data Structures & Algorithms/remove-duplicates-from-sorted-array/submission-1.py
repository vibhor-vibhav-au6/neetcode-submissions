class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        write_ptr = 1

        for curr in range(1, len(nums)):
            if nums[curr] != nums[curr-1]:
                nums[write_ptr] = nums[curr]
                write_ptr += 1
            
        return  write_ptr
