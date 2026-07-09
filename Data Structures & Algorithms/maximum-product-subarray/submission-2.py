class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        maxx = nums[0]
        minn = nums[0]
        bestmax = nums[0]

        for i in range(1, len(nums)):
            if i >= len(nums):
                return bestmax

            maxx2 = max(maxx * nums[i], minn * nums[i], nums[i])
            minn2 = min(maxx * nums[i], minn * nums[i], nums[i])

            maxx = maxx2
            minn = minn2

            if maxx2 > bestmax:
                bestmax = maxx

        return bestmax
        