class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        l = len(nums)
        res = []

        def recursion(temp, index, target, nums):
            if sum(temp) == target:
                res.append(list(temp))

            if sum(temp) > target:
                return

            
            for x in range(index, l):
                temp.append(nums[x])
                recursion(temp, x, target, nums)
                temp.pop()



        recursion([], 0, target, nums)

        return res
