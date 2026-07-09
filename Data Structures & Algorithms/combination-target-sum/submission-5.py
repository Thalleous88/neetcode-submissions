class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        l = len(nums)
        res = []

        def recursion(temp, index, target, nums):
            if target == 0:
                res.append(list(temp))
                return

            if target < 0:
                return
            
            for x in range(index, l):
                temp.append(nums[x])
                recursion(temp, x, target - nums[x], nums)
                temp.pop()



        recursion([], 0, target, nums)

        return res
