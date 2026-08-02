class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        index = 0

        def dp(index, check):
            if index >= len(nums)-1:
                return True

            if nums[index] == 0:
                return False

            temp = nums[index]
            while temp > 0:
                check = check or dp(index + temp, check)
                temp -= 1

            return check


        return dp(0, False)