class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        index = 0
        memo = {}

        def dp(index):
            if index >= len(nums)-1:
                return True

            if index in memo:
                return memo[index]

            temp = nums[index]
            while temp > 0:
                if dp(index + temp):
                    memo[index] = True
                    return True
                temp -= 1

            memo[index] = False
            return False


        return dp(0)