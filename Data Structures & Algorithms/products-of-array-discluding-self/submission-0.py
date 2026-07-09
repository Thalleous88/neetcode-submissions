class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = nums.count(0)

        tot = 1
        res = [0] * len(nums)
        
        if zeroCount > 1:
            return res

        elif zeroCount == 1:
            index = 0
            for i in range(len(nums)):
                if nums[i] != 0:
                    tot *= nums[i]
                else:
                    index = i
            res[index] = tot

            return res
        else:
            for i in range(len(nums)):
                tot *= nums[i]

            for i in range(len(nums)):
                res[i] = tot//nums[i]

            return res
        
        return res
