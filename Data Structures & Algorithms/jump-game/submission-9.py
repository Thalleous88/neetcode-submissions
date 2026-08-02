class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        index = 0

        def dp(index, check):
            if index >= len(nums)-1:
                return True

            if nums[index] == 0:
                return False

            
            for temp in range(nums[index], 0, -1):
                check = check or dp(index + temp, check)
                

            return check


        return dp(0, False)