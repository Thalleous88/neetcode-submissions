class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        l = len(nums)
        

        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
                continue        
            i += 1
            
        
        return i