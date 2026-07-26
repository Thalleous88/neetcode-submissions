class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)

        tot = 0
        for num in nums:
            check = num
            curr = 1
            while check+1 in hash_set:
                check += 1
                curr += 1

            if curr > tot:
                tot = curr

        return tot
                