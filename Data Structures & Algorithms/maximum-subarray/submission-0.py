class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        best = float('-inf')
        curr = 0
        
        for num in nums:
            curr += num

            if curr > best:
                best = curr

            if curr < 0:
                curr = 0


        return best
