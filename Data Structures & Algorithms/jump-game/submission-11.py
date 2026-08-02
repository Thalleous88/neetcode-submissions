class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        index = 0

        def dp(index):
            if index >= len(nums)-1:
                return True

            temp = nums[index]
            while temp > 0:
                if dp(index + temp):
                    return True
                temp -= 1

            return False


        return dp(0)